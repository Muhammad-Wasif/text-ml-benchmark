# app_example.py
# 30-Second Example: Connecting this dataset to your app

import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from connect import DatasetClient

def demo():
    # Step 1: Initialize the client (zero setup!)
    client = DatasetClient()
    
    print("==================================================")
    print("USE CASE 1: Fetch Data for an ML Model or LLM")
    print("==================================================")
    # Get 3 records from the 'movies_and_cinema' domain
    movies = client.get(domain="movies", limit=3)
    for m in movies:
        print(f"[{m['subtopic']}] -> {m['text'][:100]}...\n")
        
    print("==================================================")
    print("USE CASE 2: Search across all 50 domains (RAG)")
    print("==================================================")
    # Search for any topic (e.g., 'artificial intelligence' or 'cricket')
    search_results = client.search(query="climate change temperature", limit=2)
    for r in search_results:
        print(f"Domain: {r['domain']} | Subtopic: {r['subtopic']}")
        print(f"Snippet: {r['text'][:120]}...\n")

    print("==================================================")
    print("USE CASE 3: List all available domains")
    print("==================================================")
    domains = client.list_domains()
    print(f"Total domains ready to connect: {len(domains)}")
    print(f"First 10: {domains[:10]}")

if __name__ == "__main__":
    demo()
