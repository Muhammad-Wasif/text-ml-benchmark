# connect.py
# Universal, zero-dependency connector to easily plug this dataset into any Python, Node.js, Web, or Mobile app.

import os
import sys
import json
import re
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
EXPORTS_FILE = os.path.join(BASE_DIR, "data", "training_exports", "all_domains_benchmark.jsonl")
REGISTRY_FILE = os.path.join(BASE_DIR, "metadata", "dataset_registry.jsonl")

class DatasetClient:
    """
    Lightweight, high-speed client to query and stream the 50-Domain dataset.
    Requires ZERO external dependencies (pure Python standard library).
    """
    def __init__(self, data_path=EXPORTS_FILE, registry_path=REGISTRY_FILE):
        self.data_path = data_path
        self.registry_path = registry_path
        self._cache = None
        self._registry = None

    def _load_data(self):
        if self._cache is None:
            self._cache = []
            if os.path.exists(self.data_path):
                with open(self.data_path, "r", encoding="utf-8", errors="replace") as f:
                    for line in f:
                        line = line.strip()
                        if line:
                            try:
                                self._cache.append(json.loads(line))
                            except Exception:
                                pass
        return self._cache

    def _load_registry(self):
        if self._registry is None:
            self._registry = []
            if os.path.exists(self.registry_path):
                with open(self.registry_path, "r", encoding="utf-8", errors="replace") as f:
                    for line in f:
                        line = line.strip()
                        if line:
                            try:
                                self._registry.append(json.loads(line))
                            except Exception:
                                pass
        return self._registry

    def list_domains(self):
        """Returns sorted list of all 50 unique domains."""
        data = self._load_data()
        domains = sorted(list({r.get("domain") for r in data if r.get("domain")}))
        return domains

    def list_subtopics(self, domain=None):
        """Returns list of subtopics, optionally filtered by domain."""
        data = self._load_data()
        subtopics = set()
        for r in data:
            if domain is None or domain.lower() in r.get("domain", "").lower() or domain.lower() in r.get("domain_id", "").lower():
                subtopics.add((r.get("domain"), r.get("subtopic")))
        return [{"domain": d, "subtopic": s} for d, s in sorted(list(subtopics))]

    def get(self, domain=None, subtopic=None, limit=None):
        """
        Fetch records matching domain and/or subtopic filters.
        Example: client.get(domain="cricket", limit=5)
        """
        data = self._load_data()
        results = []
        d_lower = domain.lower() if domain else None
        s_lower = subtopic.lower() if subtopic else None

        for r in data:
            if d_lower:
                r_dom = r.get("domain", "").lower()
                r_did = r.get("domain_id", "").lower()
                if d_lower not in r_dom and d_lower not in r_did:
                    continue
            if s_lower:
                r_sub = r.get("subtopic", "").lower()
                r_sid = r.get("subtopic_id", "").lower()
                if s_lower not in r_sub and s_lower not in r_sid:
                    continue
            results.append(r)
            if limit and len(results) >= limit:
                break
        return results

    def search(self, query, limit=10):
        """Search text across all 50 domains and 200 subtopics."""
        data = self._load_data()
        q_tokens = [tok.lower() for tok in re.findall(r'\w+', query)]
        if not q_tokens:
            return []

        scored = []
        for r in data:
            text = (r.get("text", "") + " " + r.get("domain", "") + " " + r.get("subtopic", "")).lower()
            score = sum(text.count(tok) for tok in q_tokens)
            if score > 0:
                scored.append((score, r))

        scored.sort(key=lambda x: x[0], reverse=True)
        return [item[1] for item in scored[:limit]]

    def stats(self):
        """Summary statistics of available data."""
        data = self._load_data()
        domains = self.list_domains()
        subtopics = self.list_subtopics()
        return {
            "total_records": len(data),
            "total_domains": len(domains),
            "total_subtopics": len(subtopics),
            "file_size_bytes": os.path.getsize(self.data_path) if os.path.exists(self.data_path) else 0
        }

# ---------------------------------------------------------------------------
# Instant REST API Server (Built-in Standard Library, Zero Extra Packages)
# ---------------------------------------------------------------------------

class DatasetAPIHandler(BaseHTTPRequestHandler):
    client = DatasetClient()

    def _set_headers(self, status=200, content_type="application/json"):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers(200)

    def do_GET(self):
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)

        def get_p(key, default=None):
            val = params.get(key, [default])[0]
            return val

        if parsed.path == "/" or parsed.path == "/docs":
            self._set_headers(200, "text/html; charset=utf-8")
            html = f"""<!DOCTYPE html>
<html>
<head>
    <title>50-Domain Dataset API</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 800px; margin: 40px auto; padding: 0 20px; line-height: 1.6; background: #0f172a; color: #f8fafc; }}
        h1 {{ color: #38bdf8; }}
        code {{ background: #1e293b; padding: 3px 8px; border-radius: 4px; color: #a5f3fc; font-size: 0.9em; }}
        pre {{ background: #1e293b; padding: 15px; border-radius: 8px; overflow-x: auto; color: #e2e8f0; }}
        a {{ color: #38bdf8; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        .badge {{ display: inline-block; background: #0284c7; color: white; padding: 2px 10px; border-radius: 12px; font-size: 0.8em; font-weight: bold; }}
    </style>
</head>
<body>
    <h1>🚀 50-Domain Dataset API Server <span class="badge">Live</span></h1>
    <p>Zero-dependency REST API to plug real-world machine learning data into any application.</p>
    
    <h2>Interactive Endpoints</h2>
    <ul>
        <li><a href="/api/stats"><code>GET /api/stats</code></a> - Database summary & record counts</li>
        <li><a href="/api/domains"><code>GET /api/domains</code></a> - List all 50 domains</li>
        <li><a href="/api/subtopics"><code>GET /api/subtopics</code></a> - List all 200 subtopics</li>
        <li><a href="/api/data?domain=cricket&limit=3"><code>GET /api/data?domain=cricket&limit=3</code></a> - Query records by domain</li>
        <li><a href="/api/search?q=machine+learning&limit=5"><code>GET /api/search?q=machine+learning&limit=5</code></a> - Search across text corpus</li>
    </ul>

    <h2>Quick cURL Test</h2>
    <pre>curl "http://localhost:8000/api/data?domain=cricket&limit=2"</pre>
</body>
</html>"""
            self.wfile.write(html.encode("utf-8"))
            return

        if parsed.path == "/api/stats":
            self._set_headers(200)
            self.wfile.write(json.dumps(self.client.stats(), indent=2).encode("utf-8"))
            return

        if parsed.path == "/api/domains":
            self._set_headers(200)
            self.wfile.write(json.dumps({"domains": self.client.list_domains()}, indent=2).encode("utf-8"))
            return

        if parsed.path == "/api/subtopics":
            domain = get_p("domain")
            self._set_headers(200)
            self.wfile.write(json.dumps({"subtopics": self.client.list_subtopics(domain)}, indent=2).encode("utf-8"))
            return

        if parsed.path == "/api/data":
            domain = get_p("domain")
            subtopic = get_p("subtopic")
            limit = int(get_p("limit", 20))
            records = self.client.get(domain=domain, subtopic=subtopic, limit=limit)
            self._set_headers(200)
            self.wfile.write(json.dumps({"count": len(records), "data": records}, indent=2).encode("utf-8"))
            return

        if parsed.path == "/api/search":
            q = get_p("q", "")
            limit = int(get_p("limit", 10))
            records = self.client.search(q, limit=limit)
            self._set_headers(200)
            self.wfile.write(json.dumps({"query": q, "count": len(records), "data": records}, indent=2).encode("utf-8"))
            return

        self._set_headers(404)
        self.wfile.write(json.dumps({"error": "Endpoint not found", "available": ["/", "/api/stats", "/api/domains", "/api/subtopics", "/api/data", "/api/search"]}).encode("utf-8"))

def serve(port=8000):
    server = HTTPServer(("0.0.0.0", port), DatasetAPIHandler)
    print(f"============================================================")
    print(f"⚡ Local Dataset REST API running at: http://localhost:{port}")
    print(f"📖 Interactive Docs & Endpoints:      http://localhost:{port}/docs")
    print(f"Press Ctrl+C to stop.")
    print(f"============================================================")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
        server.server_close()

if __name__ == "__main__":
    if len(sys.argv) > 1 and ("--serve" in sys.argv or "-s" in sys.argv):
        port = 8000
        for i, arg in enumerate(sys.argv):
            if arg in ["--port", "-p"] and i + 1 < len(sys.argv):
                port = int(sys.argv[i + 1])
        serve(port)
    else:
        # CLI Demo
        client = DatasetClient()
        stats = client.stats()
        print(f"Dataset Client ready: {stats['total_domains']} domains | {stats['total_records']} records")
        print("\nTop 5 domains:")
        for d in client.list_domains()[:5]:
            print(f"  - {d}")
        print("\nSample query for 'cricket' (1 result):")
        res = client.get(domain="cricket", limit=1)
        if res:
            print(f"  Title: {res[0].get('title', res[0].get('subtopic'))}")
            print(f"  Text preview: {res[0].get('text', '')[:120]}...")
        print("\nTo start local REST API, run:")
        print("  python connect.py --serve --port 8000")
