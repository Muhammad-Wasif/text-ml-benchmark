#!/usr/bin/env python3
"""
github_data_client.py - Universal GitHub Remote Text Data Client

A lightweight, high-performance Python client and CLI to discover, preview,
access, load, stream, and download text-based datasets hosted on GitHub
without cloning the entire repository or downloading every collection.
"""

import os
import sys
import io
import re
import json
import csv
import hashlib
import urllib.parse
from typing import Dict, List, Any, Optional, Iterator, Union

import requests

# Default repository coordinates
DEFAULT_OWNER = "Muhammad-Wasif"
DEFAULT_REPO = "text-ml-benchmark"
DEFAULT_REF = "main"
DEFAULT_RAW_BASE = "https://raw.githubusercontent.com"
DEFAULT_API_BASE = "https://api.github.com"

# ---------------------------------------------------------------------------
# Custom Exceptions
# ---------------------------------------------------------------------------
class GitHubDataError(Exception):
    """Base exception for all GitHub data client errors."""
    pass

class GitHubNotFoundError(GitHubDataError):
    """Raised when a requested domain, subtopic, or file cannot be found."""
    pass

class GitHubAuthenticationError(GitHubDataError):
    """Raised when GitHub token authentication fails or access is forbidden."""
    pass

class GitHubRateLimitError(GitHubDataError):
    """Raised when GitHub API rate limits are exceeded."""
    pass

class SecurityError(GitHubDataError):
    """Raised when an invalid URL, path traversal, or SSRF attempt is detected."""
    pass


# ---------------------------------------------------------------------------
# Path & URL Security Utilities
# ---------------------------------------------------------------------------
def sanitize_path(path: str) -> str:
    """
    Sanitizes and validates a repository-relative file path.
    Prevents directory traversal, absolute paths, and null byte injection.
    """
    if not path or not isinstance(path, str):
        raise SecurityError("Path must be a non-empty string.")

    # Normalize backslashes to forward slashes
    clean = path.replace("\\", "/").strip()

    # Reject null bytes
    if "\0" in clean:
        raise SecurityError("Null bytes are forbidden in file paths.")

    # Reject absolute paths or drive letters (e.g., C:/, /etc)
    if clean.startswith("/") or re.match(r'^[a-zA-Z]:', clean):
        raise SecurityError(f"Absolute paths are forbidden: '{path}'")

    # Reject path traversal components (..)
    parts = clean.split("/")
    for part in parts:
        if part == "..":
            raise SecurityError(f"Path traversal ('..') is strictly forbidden: '{path}'")

    # Remove redundant '.' components
    normalized_parts = [p for p in parts if p and p != "."]
    if not normalized_parts:
        raise SecurityError("Invalid empty path after normalization.")

    return "/".join(normalized_parts)


def parse_github_url(url: str) -> Dict[str, Optional[str]]:
    """
    Parses any GitHub repository, file-page (blob), or raw-file URL.
    Returns a dictionary with:
      owner, repo, ref, path, is_raw
    """
    if not url or not isinstance(url, str):
        raise SecurityError("URL must be a non-empty string.")

    url = url.strip()

    # Handle short format "owner/repo"
    if re.match(r'^[a-zA-Z0-9_\-\.]+\/[a-zA-Z0-9_\-\.]+$', url):
        parts = url.split("/")
        return {
            "owner": parts[0],
            "repo": parts[1].replace(".git", ""),
            "ref": DEFAULT_REF,
            "path": None,
            "is_raw": False
        }

    parsed = urllib.parse.urlparse(url)
    netloc = parsed.netloc.lower()

    if netloc not in ["github.com", "raw.githubusercontent.com"]:
        raise SecurityError(
            f"Unsupported domain '{netloc}'. Only 'github.com' and "
            f"'raw.githubusercontent.com' are authorized."
        )

    path_parts = [p for p in parsed.path.split("/") if p]
    if len(path_parts) < 2:
        raise SecurityError(f"Invalid GitHub URL structure: '{url}'")

    owner = path_parts[0]
    repo = path_parts[1].replace(".git", "")

    # Case 1: raw.githubusercontent.com/owner/repo/ref/path...
    if netloc == "raw.githubusercontent.com":
        if len(path_parts) >= 3:
            ref = path_parts[2]
            file_path = "/".join(path_parts[3:]) if len(path_parts) > 3 else None
        else:
            ref = DEFAULT_REF
            file_path = None
        return {
            "owner": owner,
            "repo": repo,
            "ref": ref,
            "path": sanitize_path(file_path) if file_path else None,
            "is_raw": True
        }

    # Case 2: github.com/owner/repo/blob/ref/path...
    if len(path_parts) >= 4 and path_parts[2] in ["blob", "raw", "tree"]:
        ref = path_parts[3]
        file_path = "/".join(path_parts[4:]) if len(path_parts) > 4 else None
        return {
            "owner": owner,
            "repo": repo,
            "ref": ref,
            "path": sanitize_path(file_path) if file_path else None,
            "is_raw": (path_parts[2] == "raw")
        }

    # Case 3: github.com/owner/repo (base repository URL)
    return {
        "owner": owner,
        "repo": repo,
        "ref": DEFAULT_REF,
        "path": None,
        "is_raw": False
    }


def make_stable_id(path: str, domain_id: Optional[str] = None, subtopic_id: Optional[str] = None) -> str:
    """Generates a URL-safe, stable unique identifier for a file path."""
    clean = path.replace("\\", "/").strip()
    # If standard path like data/raw/01_education_and_studying/study_techniques.../file.json
    parts = clean.split("/")
    filename = parts[-1]
    if len(parts) >= 4 and parts[0] == "data" and parts[1] == "raw":
        d_part = parts[2]
        s_part = parts[3]
        base_name = re.sub(r'[^a-zA-Z0-9_\-\.]', '_', filename)
        return f"{d_part}--{s_part}--{base_name}"
    # General fallback
    clean_id = re.sub(r'[^a-zA-Z0-9_\-\.]', '_', clean)
    return clean_id


# ---------------------------------------------------------------------------
# Core Python Client: GitHubDataClient
# ---------------------------------------------------------------------------
class GitHubDataClient:
    """
    Universal client for accessing, previewing, and loading text-based datasets
    hosted on GitHub remotely without cloning or downloading the entire repository.
    """

    def __init__(
        self,
        repository_url: Optional[str] = None,
        ref: Optional[str] = None,
        token: Optional[str] = None,
        api_base_url: Optional[str] = None,
        local_fallback: bool = True,
        timeout: int = 30
    ):
        """
        Initialize the GitHubDataClient.

        :param repository_url: Full GitHub URL (e.g. 'https://github.com/Muhammad-Wasif/text-ml-benchmark')
                               or 'owner/repo'. If omitted, reads GITHUB_OWNER & GITHUB_REPO from env.
        :param ref: Branch, commit SHA, or tag name (default: 'main').
        :param token: Optional GitHub Personal Access Token (or GITHUB_TOKEN env var).
        :param api_base_url: Optional custom REST API base URL (e.g. 'http://localhost:8000').
        :param local_fallback: Whether to use local repository files if present on disk.
        :param timeout: HTTP request timeout in seconds.
        """
        # Load environment variables if present
        env_token = os.environ.get("GITHUB_TOKEN")
        env_owner = os.environ.get("GITHUB_OWNER")
        env_repo = os.environ.get("GITHUB_REPO")
        env_ref = os.environ.get("GITHUB_REF")

        self.token = token or env_token
        self.timeout = timeout
        self.local_fallback = local_fallback
        self.api_base_url = api_base_url.rstrip("/") if api_base_url else None

        # Parse repository coordinates
        if repository_url:
            parsed = parse_github_url(repository_url)
            self.owner = parsed["owner"]
            self.repo = parsed["repo"]
            self.ref = ref or parsed["ref"] or env_ref or DEFAULT_REF
        else:
            self.owner = env_owner or DEFAULT_OWNER
            self.repo = env_repo or DEFAULT_REPO
            self.ref = ref or env_ref or DEFAULT_REF

        # Session setup
        self._session = requests.Session()
        self._session.headers.update({
            "User-Agent": f"GitHubDataClient/2.0 ({self.owner}/{self.repo})"
        })
        if self.token:
            # Clean token without whitespace
            clean_tok = self.token.strip()
            self._session.headers.update({"Authorization": f"Bearer {clean_tok}"})

        # Base directories for optional local fallback
        self._local_root = os.path.abspath(os.path.dirname(__file__))
        self._is_local_available = (
            self.local_fallback and
            os.path.isdir(os.path.join(self._local_root, "data", "raw")) and
            os.path.isfile(os.path.join(self._local_root, "metadata", "dataset_registry.jsonl"))
        )

        # In-memory catalog indices
        self._catalog: List[Dict[str, Any]] = []
        self._by_id: Dict[str, Dict[str, Any]] = {}
        self._by_path: Dict[str, Dict[str, Any]] = {}
        self._by_domain: Dict[str, List[Dict[str, Any]]] = {}
        self._domains_summary: List[Dict[str, Any]] = []
        self._catalog_loaded = False

    # -----------------------------------------------------------------------
    # URL Generators
    # -----------------------------------------------------------------------
    def get_raw_url(self, path: str, ref: Optional[str] = None) -> str:
        """Constructs direct raw-content URL on raw.githubusercontent.com."""
        clean_path = sanitize_path(path)
        use_ref = ref or self.ref
        return f"{DEFAULT_RAW_BASE}/{self.owner}/{self.repo}/{use_ref}/{clean_path}"

    def get_blob_url(self, path: str, ref: Optional[str] = None) -> str:
        """Constructs GitHub web file page URL."""
        clean_path = sanitize_path(path)
        use_ref = ref or self.ref
        return f"https://github.com/{self.owner}/{self.repo}/blob/{use_ref}/{clean_path}"

    def get_api_contents_url(self, path: str, ref: Optional[str] = None) -> str:
        """Constructs GitHub REST API Contents URL."""
        clean_path = sanitize_path(path)
        use_ref = ref or self.ref
        return f"{DEFAULT_API_BASE}/repos/{self.owner}/{self.repo}/contents/{clean_path}?ref={use_ref}"

    def get_url(self, path_or_id: str, raw: bool = True, ref: Optional[str] = None) -> str:
        """Returns direct raw URL or web blob URL for a given path or file_id."""
        item = self._resolve_file_silent(path_or_id)
        path = item["path"] if item else sanitize_path(path_or_id)
        return self.get_raw_url(path, ref=ref) if raw else self.get_blob_url(path, ref=ref)

    # -----------------------------------------------------------------------
    # Internal HTTP Request Handler
    # -----------------------------------------------------------------------
    def _request(
        self,
        method: str,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        stream: bool = False,
        **kwargs
    ) -> requests.Response:
        """Executes an HTTP request with error handling and rate-limit detection."""
        req_headers = dict(self._session.headers)
        if headers:
            req_headers.update(headers)

        try:
            resp = self._session.request(
                method=method,
                url=url,
                headers=req_headers,
                stream=stream,
                timeout=self.timeout,
                **kwargs
            )
        except requests.exceptions.RequestException as e:
            raise GitHubDataError(f"Network error connecting to GitHub: {e}")

        # Rate limit inspection
        if resp.status_code == 403 and "rate limit exceeded" in resp.text.lower():
            reset_time = resp.headers.get("X-RateLimit-Reset", "unknown")
            raise GitHubRateLimitError(
                f"GitHub API rate limit exceeded. Limit resets at {reset_time}. "
                "Provide a read-only GITHUB_TOKEN to increase your rate limits."
            )

        if resp.status_code in [401, 403]:
            # Secure error message that never leaks token value
            auth_msg = "Bad credentials or access forbidden" if self.token else "Access forbidden (repository may be private)"
            raise GitHubAuthenticationError(
                f"GitHub access denied (HTTP {resp.status_code}): {auth_msg}. "
                "Ensure your token has 'Contents: Read' permission."
            )

        if resp.status_code == 404:
            raise GitHubNotFoundError(f"Requested resource not found on GitHub (HTTP 404): {url}")

        if resp.status_code >= 500:
            raise GitHubDataError(f"GitHub upstream server error (HTTP {resp.status_code})")

        return resp

    # -----------------------------------------------------------------------
    # Catalog Management & Discovery
    # -----------------------------------------------------------------------
    def load_catalog(self, refresh: bool = False) -> List[Dict[str, Any]]:
        """
        Loads and indexes the repository dataset registry.
        Uses cached catalog unless refresh=True.
        """
        if self._catalog_loaded and not refresh:
            return self._catalog

        registry_entries = []

        # 1. Try local file if local fallback enabled
        if self._is_local_available:
            local_reg = os.path.join(self._local_root, "metadata", "dataset_registry.jsonl")
            if os.path.isfile(local_reg):
                try:
                    with open(local_reg, "r", encoding="utf-8", errors="replace") as f:
                        for line in f:
                            line = line.strip()
                            if line:
                                registry_entries.append(json.loads(line))
                except Exception:
                    registry_entries = []

        # 2. Remote fetch via raw URL if local not available or empty
        if not registry_entries:
            reg_url = self.get_raw_url("metadata/dataset_registry.jsonl")
            try:
                resp = self._request("GET", reg_url)
                for line in resp.text.splitlines():
                    line = line.strip()
                    if line:
                        try:
                            registry_entries.append(json.loads(line))
                        except Exception:
                            pass
            except Exception as e:
                # 3. Fallback to GitHub Trees API if registry missing remotely
                registry_entries = self._build_catalog_from_git_tree()

        # Build index maps
        self._catalog = []
        self._by_id = {}
        self._by_path = {}
        self._by_domain = {}

        for entry in registry_entries:
            path = (entry.get("target_path") or entry.get("raw_storage_path") or "").replace("\\", "/")
            if not path:
                continue
            path = sanitize_path(path)

            domain_id = entry.get("domain_id") or (path.split("/")[2] if len(path.split("/")) > 2 else "unknown")
            subtopic_id = entry.get("subtopic_id") or "unknown"
            domain_name = entry.get("domain") or entry.get("domain_name") or domain_id.replace("_", " ").title()
            subtopic_name = entry.get("subtopic") or entry.get("subtopic_name") or "General"
            filename = entry.get("target_filename") or os.path.basename(path)
            size_bytes = entry.get("size_bytes") or entry.get("byte_size") or 0
            fmt = entry.get("format")
            if isinstance(fmt, list):
                fmt = fmt[0] if fmt else "txt"
            fmt = str(fmt or os.path.splitext(filename)[1].replace(".", "") or "txt").lower()

            candidate_title = entry.get("candidate_title") or entry.get("dataset_title") or filename
            file_id = entry.get("dataset_id") or make_stable_id(path, domain_id, subtopic_id)

            metadata_item = {
                "file_id": file_id,
                "dataset_id": entry.get("dataset_id", file_id),
                "domain_id": domain_id,
                "domain_name": domain_name,
                "subtopic_id": subtopic_id,
                "subtopic_name": subtopic_name,
                "title": candidate_title,
                "path": path,
                "filename": filename,
                "format": fmt,
                "size_bytes": size_bytes,
                "size_mb": round(size_bytes / (1024 * 1024), 2) if size_bytes else 0.0,
                "license": entry.get("license", "Unknown"),
                "source_platform": entry.get("source_platform", "External"),
                "publisher": entry.get("publisher", "Unknown"),
                "source_url": entry.get("source_url", ""),
                "raw_url": self.get_raw_url(path),
                "blob_url": self.get_blob_url(path),
                "sha256": entry.get("sha256", ""),
                "ref": self.ref,
                "available": True
            }

            self._catalog.append(metadata_item)
            self._by_id[file_id] = metadata_item
            self._by_path[path] = metadata_item
            # Also register secondary clean ID if different
            clean_alt_id = make_stable_id(path)
            if clean_alt_id not in self._by_id:
                self._by_id[clean_alt_id] = metadata_item

            if domain_id not in self._by_domain:
                self._by_domain[domain_id] = []
            self._by_domain[domain_id].append(metadata_item)

        self._catalog_loaded = True
        return self._catalog

    def _build_catalog_from_git_tree(self) -> List[Dict[str, Any]]:
        """Fallback: uses GitHub Git Trees API to discover files in data/raw/."""
        tree_url = f"{DEFAULT_API_BASE}/repos/{self.owner}/{self.repo}/git/trees/{self.ref}?recursive=1"
        resp = self._request("GET", tree_url)
        data = resp.json()
        tree = data.get("tree", [])

        discovered = []
        for item in tree:
            if item.get("type") == "blob":
                path = item.get("path", "")
                if path.startswith("data/raw/") and not path.endswith("README.md"):
                    parts = path.split("/")
                    domain_id = parts[2] if len(parts) > 2 else "unknown"
                    subtopic_id = parts[3] if len(parts) > 3 else "unknown"
                    fn = os.path.basename(path)
                    discovered.append({
                        "domain_id": domain_id,
                        "subtopic_id": subtopic_id,
                        "raw_storage_path": path,
                        "target_filename": fn,
                        "size_bytes": item.get("size", 0),
                        "sha256": item.get("sha", "")
                    })
        return discovered

    def _resolve_file_silent(self, path_or_id: str) -> Optional[Dict[str, Any]]:
        """Resolves path, file_id, or URL into a catalog item without throwing."""
        if not self._catalog_loaded:
            self.load_catalog()

        # 1. URL check
        if path_or_id.startswith("http://") or path_or_id.startswith("https://"):
            try:
                parsed = parse_github_url(path_or_id)
                if parsed.get("path"):
                    path_or_id = parsed["path"]
            except SecurityError:
                return None

        # 2. Exact file_id match
        if path_or_id in self._by_id:
            return self._by_id[path_or_id]

        # 3. Exact path match (normalized)
        norm_path = path_or_id.replace("\\", "/").strip().lstrip("/")
        if norm_path in self._by_path:
            return self._by_path[norm_path]

        # 4. Partial filename or suffix match
        for p, item in self._by_path.items():
            if p.endswith(norm_path) or item["filename"] == norm_path:
                return item

        return None

    def _resolve_file(self, path_or_id: str) -> Dict[str, Any]:
        """Resolves path, file_id, or URL into a catalog item, raising 404 if missing."""
        # 1. Security check first: if it attempts directory traversal or absolute path, raise SecurityError
        if ".." in path_or_id or path_or_id.startswith("/") or re.match(r'^[a-zA-Z]:', path_or_id):
            sanitize_path(path_or_id)  # Will raise SecurityError directly

        # 2. Check catalog
        item = self._resolve_file_silent(path_or_id)
        if item:
            return item

        # 3. If not in catalog, check if it's a valid path that actually exists locally or remotely
        clean = sanitize_path(path_or_id)
        local_path = os.path.join(self._local_root, clean)
        if self._is_local_available and os.path.isfile(local_path):
            fn = os.path.basename(clean)
            sz = os.path.getsize(local_path)
            return {
                "file_id": make_stable_id(clean),
                "dataset_id": make_stable_id(clean),
                "domain_id": clean.split("/")[2] if len(clean.split("/")) > 2 else "custom",
                "domain_name": "Custom Domain",
                "subtopic_id": "custom",
                "subtopic_name": "Custom Subtopic",
                "title": fn,
                "path": clean,
                "filename": fn,
                "format": os.path.splitext(fn)[1].replace(".", "").lower() or "txt",
                "size_bytes": sz,
                "size_mb": round(sz / (1024 * 1024), 2),
                "license": "Unspecified",
                "source_platform": "Local Repository",
                "publisher": self.owner,
                "source_url": self.get_blob_url(clean),
                "raw_url": self.get_raw_url(clean),
                "blob_url": self.get_blob_url(clean),
                "sha256": "",
                "ref": self.ref,
                "available": True
            }

        # 4. If it has path separators and extension, check remote repository
        if "/" in clean and "." in clean:
            raw_url = self.get_raw_url(clean)
            try:
                resp = self._request("HEAD", raw_url)
                if resp.status_code == 200:
                    fn = os.path.basename(clean)
                    sz = int(resp.headers.get("content-length", 0))
                    return {
                        "file_id": make_stable_id(clean),
                        "dataset_id": make_stable_id(clean),
                        "domain_id": clean.split("/")[2] if len(clean.split("/")) > 2 else "custom",
                        "domain_name": "Custom Domain",
                        "subtopic_id": "custom",
                        "subtopic_name": "Custom Subtopic",
                        "title": fn,
                        "path": clean,
                        "filename": fn,
                        "format": os.path.splitext(fn)[1].replace(".", "").lower() or "txt",
                        "size_bytes": sz,
                        "size_mb": round(sz / (1024 * 1024), 2),
                        "license": "Unspecified",
                        "source_platform": "GitHub Repository",
                        "publisher": self.owner,
                        "source_url": self.get_blob_url(clean),
                        "raw_url": raw_url,
                        "blob_url": self.get_blob_url(clean),
                        "sha256": "",
                        "ref": self.ref,
                        "available": True
                    }
            except Exception:
                pass

        raise GitHubNotFoundError(f"File or dataset '{path_or_id}' was not found in the catalog or repository.")

    # -----------------------------------------------------------------------
    # Public Discovery API
    # -----------------------------------------------------------------------
    def list_domains(self) -> List[Dict[str, Any]]:
        """Returns sorted list of all 50 available domains with file metrics."""
        self.load_catalog()
        summary = []
        for did in sorted(self._by_domain.keys()):
            files = self._by_domain[did]
            subtopics = sorted(list({f["subtopic_name"] for f in files}))
            total_size = sum(f.get("size_bytes", 0) for f in files)
            dname = files[0]["domain_name"] if files else did.replace("_", " ").title()
            summary.append({
                "domain_id": did,
                "domain_name": dname,
                "subtopics_count": len(subtopics),
                "files_count": len(files),
                "total_size_bytes": total_size,
                "total_size_mb": round(total_size / (1024 * 1024), 2),
                "subtopics": subtopics
            })
        return summary

    def list_subtopics(self, domain: Optional[str] = None) -> List[Dict[str, Any]]:
        """Returns list of subtopics, optionally filtered by domain."""
        self.load_catalog()
        subtopics_map = {}
        d_lower = domain.lower() if domain else None

        for item in self._catalog:
            did = item["domain_id"]
            dname = item["domain_name"]
            sid = item["subtopic_id"]
            sname = item["subtopic_name"]

            if d_lower:
                if d_lower not in did.lower() and d_lower not in dname.lower():
                    continue

            key = (did, sname)
            if key not in subtopics_map:
                subtopics_map[key] = {
                    "domain_id": did,
                    "domain_name": dname,
                    "subtopic_id": sid,
                    "subtopic_name": sname,
                    "files_count": 0,
                    "total_size_bytes": 0
                }
            subtopics_map[key]["files_count"] += 1
            subtopics_map[key]["total_size_bytes"] += item.get("size_bytes", 0)

        results = list(subtopics_map.values())
        for r in results:
            r["total_size_mb"] = round(r["total_size_bytes"] / (1024 * 1024), 2)
        return sorted(results, key=lambda x: (x["domain_id"], x["subtopic_name"]))

    def list_files(
        self,
        domain: Optional[str] = None,
        subtopic: Optional[str] = None,
        format: Optional[str] = None,
        limit: Optional[int] = None,
        offset: int = 0
    ) -> List[Dict[str, Any]]:
        """Lists files with optional filtering by domain, subtopic, and format."""
        self.load_catalog()
        d_lower = domain.lower() if domain else None
        s_lower = subtopic.lower() if subtopic else None
        f_lower = format.lower() if format else None

        filtered = []
        for item in self._catalog:
            if d_lower and (d_lower not in item["domain_id"].lower() and d_lower not in item["domain_name"].lower()):
                continue
            if s_lower and (s_lower not in item["subtopic_id"].lower() and s_lower not in item["subtopic_name"].lower()):
                continue
            if f_lower and item["format"].lower() != f_lower:
                continue
            filtered.append(item)

        if offset:
            filtered = filtered[offset:]
        if limit:
            filtered = filtered[:limit]
        return filtered

    def search(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Searches files by keyword across domain, subtopic, title, and filename."""
        self.load_catalog()
        tokens = [t.lower() for t in re.findall(r'\w+', query)]
        if not tokens:
            return []

        scored = []
        for item in self._catalog:
            searchable = (
                f"{item['domain_id']} {item['domain_name']} {item['subtopic_name']} "
                f"{item['title']} {item['filename']} {item['license']} {item['source_platform']}"
            ).lower()
            score = sum(searchable.count(t) for t in tokens)
            if score > 0:
                scored.append((score, item))

        scored.sort(key=lambda x: x[0], reverse=True)
        return [item[1] for item in scored[:limit]]

    def get_file_info(self, path_or_id: str) -> Dict[str, Any]:
        """Returns full metadata for an individual file."""
        return self._resolve_file(path_or_id)

    # -----------------------------------------------------------------------
    # Memory-Efficient Preview Engine
    # -----------------------------------------------------------------------
    def preview(self, path_or_id: str, limit: int = 20, max_bytes: int = 65536) -> Dict[str, Any]:
        """
        Retrieves a memory-efficient bounded preview of a text dataset file.
        Uses HTTP Range requests to fetch only initial bytes without downloading
        the complete file into memory.

        :param path_or_id: File path, file_id, or GitHub URL.
        :param limit: Maximum rows, lines, or records to return (capped at 100).
        :param max_bytes: Maximum byte slice to fetch remotely (default: 64 KB).
        """
        limit = min(max(1, limit), 100)
        item = self._resolve_file(path_or_id)
        path = item["path"]
        fmt = item["format"].lower()

        raw_bytes = b""
        is_partial = False

        # 1. Local fallback if file exists on disk
        local_path = os.path.join(self._local_root, path)
        if self._is_local_available and os.path.isfile(local_path):
            with open(local_path, "rb") as f:
                raw_bytes = f.read(max_bytes)
            is_partial = os.path.getsize(local_path) > len(raw_bytes)
        else:
            # 2. Remote Range request
            raw_url = item["raw_url"]
            range_header = {"Range": f"bytes=0-{max_bytes - 1}"}
            try:
                resp = self._request("GET", raw_url, headers=range_header)
                raw_bytes = resp.content
                is_partial = (resp.status_code == 206)
            except Exception:
                # Fallback to standard request with stream
                resp = self._request("GET", raw_url, stream=True)
                raw_bytes = next(resp.iter_content(chunk_size=max_bytes), b"")
                is_partial = True

        text_snippet = raw_bytes.decode("utf-8", errors="replace")

        # Parse preview based on format
        preview_data: Any = None
        columns: Optional[List[str]] = None

        if fmt in ["csv", "tsv"]:
            delimiter = "\t" if fmt == "tsv" else ","
            sio = io.StringIO(text_snippet)
            reader = csv.reader(sio, delimiter=delimiter)
            rows = []
            try:
                columns = next(reader, [])
                for row in reader:
                    if len(rows) >= limit:
                        break
                    # If this is the last row of a partial fetch and column count doesn't match, drop incomplete row
                    if is_partial and columns and len(row) != len(columns) and len(rows) > 0:
                        continue
                    rows.append(row)
            except Exception:
                pass
            preview_data = {
                "columns": columns,
                "rows": rows,
                "total_columns": len(columns) if columns else 0,
                "row_count_previewed": len(rows)
            }

        elif fmt == "jsonl":
            lines = text_snippet.splitlines()
            records = []
            for line in lines:
                if len(records) >= limit:
                    break
                line = line.strip()
                if line:
                    try:
                        records.append(json.loads(line))
                    except Exception:
                        pass
            preview_data = records

        elif fmt == "json":
            try:
                # Try parsing the whole snippet
                full_json = json.loads(text_snippet)
                if isinstance(full_json, list):
                    preview_data = full_json[:limit]
                elif isinstance(full_json, dict):
                    # Show keys and bounded values
                    preview_data = {k: full_json[k] for k in list(full_json.keys())[:limit]}
                else:
                    preview_data = full_json
            except Exception:
                # Return bounded textual lines
                lines = [l for l in text_snippet.splitlines() if l.strip()][:limit]
                preview_data = "\n".join(lines)

        else:
            # Plain text, Markdown, XML, ARFF
            lines = text_snippet.splitlines()[:limit]
            preview_data = "\n".join(lines)

        return {
            "file_id": item["file_id"],
            "path": path,
            "filename": item["filename"],
            "format": fmt,
            "size_bytes": item["size_bytes"],
            "limit": limit,
            "is_truncated": is_partial or (len(raw_bytes) >= max_bytes),
            "preview_data": preview_data,
            "metadata": item
        }

    # -----------------------------------------------------------------------
    # Content Reading & Tabular Loading
    # -----------------------------------------------------------------------
    def read_text(self, path_or_id: str, encoding: str = "utf-8") -> str:
        """Retrieves complete text contents of a dataset file."""
        item = self._resolve_file(path_or_id)
        path = item["path"]

        # Local fallback
        local_path = os.path.join(self._local_root, path)
        if self._is_local_available and os.path.isfile(local_path):
            with open(local_path, "r", encoding=encoding, errors="replace") as f:
                return f.read()

        # Remote fetch
        resp = self._request("GET", item["raw_url"])
        return resp.content.decode(encoding, errors="replace")

    def load_table(self, path_or_id: str, **kwargs) -> Any:
        """
        Loads tabular data into a pandas DataFrame (CSV, TSV, JSON, Parquet).
        If pandas is not installed, returns parsed Python structures.
        """
        item = self._resolve_file(path_or_id)
        fmt = item["format"].lower()

        # Try pandas import
        try:
            import pandas as pd
            has_pandas = True
        except ImportError:
            has_pandas = False

        if not has_pandas:
            # Fallback for CSV without pandas
            text = self.read_text(path_or_id)
            if fmt in ["csv", "tsv"]:
                delim = "\t" if fmt == "tsv" else ","
                reader = csv.DictReader(io.StringIO(text), delimiter=delim)
                return list(reader)
            elif fmt in ["json", "jsonl"]:
                if fmt == "jsonl":
                    return [json.loads(l) for l in text.splitlines() if l.strip()]
                return json.loads(text)
            else:
                return text

        # Pandas execution
        if fmt == "csv":
            text = self.read_text(path_or_id)
            return pd.read_csv(io.StringIO(text), **kwargs)
        elif fmt == "tsv":
            text = self.read_text(path_or_id)
            return pd.read_csv(io.StringIO(text), sep="\t", **kwargs)
        elif fmt == "jsonl":
            text = self.read_text(path_or_id)
            return pd.read_json(io.StringIO(text), lines=True, **kwargs)
        elif fmt == "json":
            text = self.read_text(path_or_id)
            return pd.read_json(io.StringIO(text), **kwargs)
        elif fmt == "parquet":
            # For binary Parquet, fetch raw bytes
            raw_url = item["raw_url"]
            resp = self._request("GET", raw_url)
            return pd.read_parquet(io.BytesIO(resp.content), **kwargs)
        else:
            raise GitHubDataError(f"Format '{fmt}' is not directly convertible to a DataFrame. Use read_text().")

    def stream_lines(self, path_or_id: str, chunk_size: int = 8192) -> Iterator[str]:
        """Streams lines from a remote or local text file without loading it entirely into RAM."""
        item = self._resolve_file(path_or_id)
        path = item["path"]

        local_path = os.path.join(self._local_root, path)
        if self._is_local_available and os.path.isfile(local_path):
            with open(local_path, "r", encoding="utf-8", errors="replace") as f:
                for line in f:
                    yield line
            return

        resp = self._request("GET", item["raw_url"], stream=True)
        for line in resp.iter_lines(chunk_size=chunk_size, decode_unicode=True):
            if line:
                yield line

    def stream_records(self, path_or_id: str) -> Iterator[Dict[str, Any]]:
        """Streams parsed JSON objects from a JSONL file line-by-line."""
        for line in self.stream_lines(path_or_id):
            line = line.strip()
            if line:
                try:
                    yield json.loads(line)
                except Exception:
                    pass

    # -----------------------------------------------------------------------
    # Single-File Downloading with Checksum Verification
    # -----------------------------------------------------------------------
    def download(
        self,
        path_or_id: str,
        destination: Optional[str] = None,
        verify_checksum: bool = True,
        chunk_size: int = 65536
    ) -> Dict[str, Any]:
        """
        Downloads ONLY the requested individual data file to a local destination.

        :param path_or_id: Path, file_id, or GitHub URL.
        :param destination: Local file path (defaults to current directory with filename).
        :param verify_checksum: If True, computes and checks SHA-256 against registry.
        """
        item = self._resolve_file(path_or_id)
        dest = destination or os.path.join(os.getcwd(), item["filename"])
        dest = os.path.abspath(dest)

        # Create parent directories
        os.makedirs(os.path.dirname(dest), exist_ok=True)

        sha = hashlib.sha256()
        total_bytes = 0

        # Stream write
        local_path = os.path.join(self._local_root, item["path"])
        if self._is_local_available and os.path.isfile(local_path):
            with open(local_path, "rb") as src, open(dest, "wb") as dst:
                while chunk := src.read(chunk_size):
                    dst.write(chunk)
                    sha.update(chunk)
                    total_bytes += len(chunk)
        else:
            resp = self._request("GET", item["raw_url"], stream=True)
            with open(dest, "wb") as f:
                for chunk in resp.iter_content(chunk_size=chunk_size):
                    if chunk:
                        f.write(chunk)
                        sha.update(chunk)
                        total_bytes += len(chunk)

        computed_sha = sha.hexdigest()
        expected_sha = item.get("sha256")
        verified = True

        if verify_checksum and expected_sha:
            matches = (computed_sha.lower() == expected_sha.lower())
            if not matches:
                # Check cross-platform line ending normalization (CRLF <-> LF)
                try:
                    with open(dest, "rb") as f:
                        c_bytes = f.read()
                    h_lf = hashlib.sha256(c_bytes.replace(b"\r\n", b"\n")).hexdigest()
                    h_crlf = hashlib.sha256(c_bytes.replace(b"\n", b"\r\n")).hexdigest()
                    if expected_sha.lower() in [h_lf.lower(), h_crlf.lower()]:
                        matches = True
                except Exception:
                    pass

            if not matches:
                verified = False
                raise GitHubDataError(
                    f"SHA-256 integrity check failed for '{item['filename']}': "
                    f"expected {expected_sha}, got {computed_sha}"
                )

        return {
            "status": "success",
            "file_id": item["file_id"],
            "filename": item["filename"],
            "destination": dest,
            "size_bytes": total_bytes,
            "sha256": computed_sha,
            "checksum_verified": verified
        }


# ---------------------------------------------------------------------------
# Command Line Interface (CLI)
# ---------------------------------------------------------------------------
def main():
    import argparse

    parser = argparse.ArgumentParser(
        prog="github-data-client",
        description="CLI for Remote GitHub Text Dataset Benchmark"
    )
    parser.add_argument("--repo", default=None, help="GitHub repository URL or 'owner/repo'")
    parser.add_argument("--ref", default=None, help="Branch, tag, or commit SHA (default: main)")
    parser.add_argument("--token", default=None, help="GitHub Personal Access Token")

    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # Command: domains
    subparsers.add_parser("domains", help="List all 50 available domains")

    # Command: subtopics
    sub_p = subparsers.add_parser("subtopics", help="List subtopics for a domain")
    sub_p.add_argument("--domain", "-d", required=False, help="Domain ID or name")

    # Command: files
    f_p = subparsers.add_parser("files", help="List dataset files")
    f_p.add_argument("--domain", "-d", help="Filter by domain")
    f_p.add_argument("--subtopic", "-s", help="Filter by subtopic")
    f_p.add_argument("--format", "-f", help="Filter by format (e.g. csv, json, txt)")
    f_p.add_argument("--limit", "-l", type=int, default=20, help="Max results (default: 20)")

    # Command: search
    s_p = subparsers.add_parser("search", help="Search datasets by keyword")
    s_p.add_argument("query", help="Search query string")
    s_p.add_argument("--limit", "-l", type=int, default=10, help="Max results")

    # Command: preview
    p_p = subparsers.add_parser("preview", help="Preview a file without downloading all collections")
    p_p.add_argument("path_or_id", help="Path, file_id, or GitHub URL")
    p_p.add_argument("--limit", "-l", type=int, default=10, help="Number of rows/lines (default: 10)")

    # Command: read
    r_p = subparsers.add_parser("read", help="Print complete text content to stdout")
    r_p.add_argument("path_or_id", help="Path, file_id, or GitHub URL")
    r_p.add_argument("--head", type=int, default=None, help="Truncate to first N characters")

    # Command: download
    d_p = subparsers.add_parser("download", help="Download only a single selected file")
    d_p.add_argument("path_or_id", help="Path, file_id, or GitHub URL")
    d_p.add_argument("--out", "-o", default=None, help="Destination local file path")

    # Command: url
    u_p = subparsers.add_parser("url", help="Get direct raw and blob URLs for a file")
    u_p.add_argument("path_or_id", help="Path, file_id, or GitHub URL")

    # Command: serve
    srv_p = subparsers.add_parser("serve", help="Launch the local FastAPI REST API server")
    srv_p.add_argument("--host", default="0.0.0.0", help="Host address (default: 0.0.0.0)")
    srv_p.add_argument("--port", type=int, default=8000, help="Port (default: 8000)")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(0)

    if args.command == "serve":
        try:
            import uvicorn
            print(f"Starting FastAPI REST API server on http://{args.host}:{args.port} ...")
            uvicorn.run("api:app", host=args.host, port=args.port, reload=False)
        except ImportError:
            print("Error: uvicorn is required to run the API server. Install with 'pip install uvicorn fastapi'.")
            sys.exit(1)
        return

    client = GitHubDataClient(
        repository_url=args.repo,
        ref=args.ref,
        token=args.token
    )

    if args.command == "domains":
        domains = client.list_domains()
        print(f"\n{'DOMAIN ID':40s} | {'SUBTOPICS':10s} | {'FILES':6s} | {'SIZE (MB)':10s}")
        print("-" * 75)
        for d in domains:
            print(f"{d['domain_id']:40s} | {d['subtopics_count']:<10d} | {d['files_count']:<6d} | {d['total_size_mb']:<10.2f}")
        print(f"\nTotal Domains: {len(domains)}")

    elif args.command == "subtopics":
        subtopics = client.list_subtopics(args.domain)
        print(f"\n{'DOMAIN':35s} | {'SUBTOPIC':40s} | {'FILES':6s}")
        print("-" * 88)
        for s in subtopics:
            print(f"{s['domain_name'][:35]:35s} | {s['subtopic_name'][:40]:40s} | {s['files_count']:<6d}")

    elif args.command == "files":
        files = client.list_files(
            domain=args.domain,
            subtopic=args.subtopic,
            format=args.format,
            limit=args.limit
        )
        print(f"\n{'FORMAT':8s} | {'SIZE (KB)':10s} | {'FILE ID / PATH'}")
        print("-" * 75)
        for f in files:
            sz_kb = round(f['size_bytes'] / 1024, 1)
            print(f"{f['format'].upper():8s} | {sz_kb:<10.1f} | {f['path']}")
        print(f"\nShowing {len(files)} files.")

    elif args.command == "search":
        matches = client.search(args.query, limit=args.limit)
        print(f"\nFound {len(matches)} search results for '{args.query}':\n")
        for m in matches:
            print(f"[{m['format'].upper()}] {m['title']}")
            print(f"  Path:   {m['path']}")
            print(f"  Domain: {m['domain_name']} -> {m['subtopic_name']}\n")

    elif args.command == "preview":
        res = client.preview(args.path_or_id, limit=args.limit)
        print(f"\n=== PREVIEW: {res['filename']} ({res['format'].upper()}) ===")
        print(f"Path: {res['path']}")
        print(f"Size: {res['size_bytes']:,} bytes | Truncated: {res['is_truncated']}\n")
        if isinstance(res["preview_data"], dict) and "columns" in res["preview_data"]:
            print(f"Columns: {res['preview_data']['columns']}")
            print(f"Sample Rows (first {len(res['preview_data']['rows'])}):")
            for r in res["preview_data"]["rows"]:
                print(" ", r)
        elif isinstance(res["preview_data"], list):
            print(json.dumps(res["preview_data"], indent=2))
        else:
            print(res["preview_data"])

    elif args.command == "read":
        txt = client.read_text(args.path_or_id)
        if args.head:
            print(txt[:args.head])
        else:
            print(txt)

    elif args.command == "download":
        res = client.download(args.path_or_id, destination=args.out)
        print(f"\nSuccessfully downloaded single file:")
        print(f"  Destination: {res['destination']}")
        print(f"  Size:        {res['size_bytes']:,} bytes")
        print(f"  SHA-256:     {res['sha256']}")

    elif args.command == "url":
        info = client.get_file_info(args.path_or_id)
        print(f"\nFile: {info['filename']}")
        print(f"  Raw URL:  {info['raw_url']}")
        print(f"  Web URL:  {info['blob_url']}")


if __name__ == "__main__":
    main()
