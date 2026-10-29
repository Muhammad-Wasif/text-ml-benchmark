#!/usr/bin/env python3
"""
api.py - FastAPI Remote Text Data Access Service

Provides a REST API for discovering, previewing, reading, streaming,
and downloading dataset files from the GitHub repository Muhammad-Wasif/text-ml-benchmark.
"""

import os
import sys
import time
from typing import Optional, List, Dict, Any

from fastapi import FastAPI, HTTPException, Query, Header, Depends, status, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, PlainTextResponse, StreamingResponse
from pydantic import BaseModel, Field

from github_data_client import (
    GitHubDataClient,
    GitHubDataError,
    GitHubNotFoundError,
    GitHubAuthenticationError,
    GitHubRateLimitError,
    SecurityError,
    sanitize_path
)

# ---------------------------------------------------------------------------
# App Initialization & Configuration
# ---------------------------------------------------------------------------
app = FastAPI(
    title="Text ML Benchmark Remote Data Access API",
    description=(
        "Production REST API to remotely discover, preview, load, and download "
        "real-world text datasets across 50 domains and 200 subtopics from GitHub."
    ),
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Enable CORS for web apps and notebooks
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "OPTIONS"],
    allow_headers=["*"],
)

# Shared Client Instance
client = GitHubDataClient()

# Security API Key Check
EXPECTED_API_KEY = os.environ.get("API_KEY", "").strip()

def verify_api_key(x_api_key: Optional[str] = Header(None)):
    """Optional API Key verification if API_KEY is configured in environment."""
    if EXPECTED_API_KEY:
        if not x_api_key or x_api_key.strip() != EXPECTED_API_KEY:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Unauthorized: Valid X-API-Key header required."
            )
    return True


# ---------------------------------------------------------------------------
# Response Models
# ---------------------------------------------------------------------------
class HealthResponse(BaseModel):
    status: str
    repository: str
    owner: str
    ref: str
    total_datasets: int
    uptime_seconds: float
    timestamp: float

class DomainInfo(BaseModel):
    domain_id: str
    domain_name: str
    subtopics_count: int
    files_count: int
    total_size_mb: float
    subtopics: List[str]

class SubtopicInfo(BaseModel):
    domain_id: str
    domain_name: str
    subtopic_id: str
    subtopic_name: str
    files_count: int
    total_size_mb: float

class FileMetadataModel(BaseModel):
    file_id: str
    dataset_id: str
    domain_id: str
    domain_name: str
    subtopic_id: str
    subtopic_name: str
    title: str
    path: str
    filename: str
    format: str
    size_bytes: int
    size_mb: float
    license: str
    source_platform: str
    publisher: str
    source_url: str
    raw_url: str
    blob_url: str
    sha256: str
    ref: str
    available: bool

class FileListResponse(BaseModel):
    total_matching: int
    limit: int
    offset: int
    files: List[FileMetadataModel]

class PreviewResponse(BaseModel):
    file_id: str
    path: str
    filename: str
    format: str
    size_bytes: int
    limit: int
    is_truncated: bool
    preview_data: Any
    metadata: Dict[str, Any]

class FileUrlsResponse(BaseModel):
    file_id: str
    path: str
    filename: str
    raw_url: str
    blob_url: str
    api_contents_url: str

START_TIME = time.time()


# ---------------------------------------------------------------------------
# API Routes: /api/v1/...
# ---------------------------------------------------------------------------
@app.get("/api/v1/health", response_model=HealthResponse, tags=["System"])
def get_health():
    """Health check endpoint providing repository status and catalog size."""
    catalog = client.load_catalog()
    return HealthResponse(
        status="healthy",
        repository=f"{client.owner}/{client.repo}",
        owner=client.owner,
        ref=client.ref,
        total_datasets=len(catalog),
        uptime_seconds=round(time.time() - START_TIME, 2),
        timestamp=time.time()
    )


@app.get("/api/v1/domains", response_model=List[DomainInfo], tags=["Discovery"])
def get_domains(_: bool = Depends(verify_api_key)):
    """Lists all 50 available real-world domains with file counts and storage metrics."""
    return client.list_domains()


@app.get("/api/v1/domains/{domain}/subtopics", response_model=List[SubtopicInfo], tags=["Discovery"])
def get_domain_subtopics(domain: str, _: bool = Depends(verify_api_key)):
    """Lists all subtopics within a specified domain."""
    subtopics = client.list_subtopics(domain=domain)
    if not subtopics:
        raise HTTPException(status_code=404, detail=f"Domain '{domain}' not found.")
    return subtopics


@app.get("/api/v1/files", response_model=FileListResponse, tags=["Discovery"])
def get_files(
    domain: Optional[str] = Query(None, description="Filter by domain ID or name"),
    subtopic: Optional[str] = Query(None, description="Filter by subtopic ID or name"),
    format: Optional[str] = Query(None, description="Filter by file format (e.g. csv, json, txt)"),
    q: Optional[str] = Query(None, description="Search query string across metadata"),
    limit: int = Query(20, ge=1, le=100, description="Pagination limit (max 100)"),
    offset: int = Query(0, ge=0, description="Pagination offset"),
    _: bool = Depends(verify_api_key)
):
    """
    Search and filter data files across all domains and subtopics.
    Supports keyword search and metadata filtering.
    """
    if q:
        items = client.search(q, limit=limit + offset)
        if domain or subtopic or format:
            d_l = domain.lower() if domain else None
            s_l = subtopic.lower() if subtopic else None
            f_l = format.lower() if format else None
            filtered = []
            for item in items:
                if d_l and (d_l not in item["domain_id"].lower() and d_l not in item["domain_name"].lower()):
                    continue
                if s_l and (s_l not in item["subtopic_id"].lower() and s_l not in item["subtopic_name"].lower()):
                    continue
                if f_l and item["format"].lower() != f_l:
                    continue
                filtered.append(item)
            items = filtered
    else:
        items = client.list_files(domain=domain, subtopic=subtopic, format=format)

    total = len(items)
    paginated = items[offset:offset + limit]

    return FileListResponse(
        total_matching=total,
        limit=limit,
        offset=offset,
        files=paginated
    )


@app.get("/api/v1/files/{file_id}", response_model=FileMetadataModel, tags=["Files"])
def get_file_metadata(file_id: str, _: bool = Depends(verify_api_key)):
    """Retrieves verified metadata for an individual dataset file."""
    try:
        return client.get_file_info(file_id)
    except GitHubNotFoundError:
        raise HTTPException(status_code=404, detail=f"File with ID or path '{file_id}' not found.")
    except SecurityError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/api/v1/files/{file_id}/preview", response_model=PreviewResponse, tags=["Files"])
def get_file_preview(
    file_id: str,
    limit: int = Query(20, ge=1, le=100, description="Max rows, lines, or records to preview"),
    _: bool = Depends(verify_api_key)
):
    """
    Returns a memory-efficient preview of the file contents.
    Fetches only a partial byte slice remotely without loading entire collections.
    """
    try:
        return client.preview(file_id, limit=limit)
    except GitHubNotFoundError:
        raise HTTPException(status_code=404, detail=f"File '{file_id}' not found.")
    except SecurityError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error previewing file: {e}")


@app.get("/api/v1/files/{file_id}/content", tags=["Files"])
def get_file_content(file_id: str, _: bool = Depends(verify_api_key)):
    """Retrieves the full text content of a dataset file with proper MIME headers."""
    try:
        info = client.get_file_info(file_id)
        text = client.read_text(file_id)
        fmt = info.get("format", "txt").lower()

        media_types = {
            "json": "application/json; charset=utf-8",
            "jsonl": "application/x-ndjson; charset=utf-8",
            "csv": "text/csv; charset=utf-8",
            "tsv": "text/tab-separated-values; charset=utf-8",
            "txt": "text/plain; charset=utf-8",
            "md": "text/markdown; charset=utf-8",
            "xml": "application/xml; charset=utf-8"
        }
        media_type = media_types.get(fmt, "text/plain; charset=utf-8")
        return Response(content=text, media_type=media_type)
    except GitHubNotFoundError:
        raise HTTPException(status_code=404, detail=f"File '{file_id}' not found.")
    except SecurityError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving content: {e}")


@app.get("/api/v1/files/{file_id}/download", tags=["Files"])
def download_file_stream(file_id: str, _: bool = Depends(verify_api_key)):
    """Streams the requested file as a browser download attachment."""
    try:
        info = client.get_file_info(file_id)
        filename = info.get("filename", "download.txt")

        def file_iterator():
            for line in client.stream_lines(file_id):
                yield (line + "\n").encode("utf-8")

        headers = {
            "Content-Disposition": f'attachment; filename="{filename}"'
        }
        return StreamingResponse(file_iterator(), media_type="application/octet-stream", headers=headers)
    except GitHubNotFoundError:
        raise HTTPException(status_code=404, detail=f"File '{file_id}' not found.")
    except SecurityError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/api/v1/files/{file_id}/url", response_model=FileUrlsResponse, tags=["Files"])
def get_file_urls(file_id: str, _: bool = Depends(verify_api_key)):
    """Returns direct raw URL, GitHub web page URL, and GitHub REST API URL."""
    try:
        info = client.get_file_info(file_id)
        path = info["path"]
        return FileUrlsResponse(
            file_id=info["file_id"],
            path=path,
            filename=info["filename"],
            raw_url=client.get_raw_url(path),
            blob_url=client.get_blob_url(path),
            api_contents_url=client.get_api_contents_url(path)
        )
    except GitHubNotFoundError:
        raise HTTPException(status_code=404, detail=f"File '{file_id}' not found.")
    except SecurityError as e:
        raise HTTPException(status_code=400, detail=str(e))


# ---------------------------------------------------------------------------
# Server Entrypoint
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    import uvicorn
    host = os.environ.get("API_HOST", "0.0.0.0")
    port = int(os.environ.get("API_PORT", 8000))
    print(f"Starting Text ML Benchmark API Server on http://{host}:{port} ...")
    uvicorn.run("api:app", host=host, port=port, reload=False)
