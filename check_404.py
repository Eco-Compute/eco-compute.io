#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

start_url = "http://localhost:1313"
visited = set()
to_visit = [start_url]

while to_visit:
    url = to_visit.pop()
    if url in visited:
        continue
    visited.add(url)

    try:
        r = requests.get(url)
        if r.status_code == 404:
            print(f"404: {url}")
            continue
    except requests.RequestException as e:
        print(f"Error: {url} -> {e}")
        continue

    soup = BeautifulSoup(r.text, "html.parser")
    for link in soup.find_all("a", href=True):
        href = link["href"]
        full_url = urljoin(url, href)
        # Only follow internal links
        if urlparse(full_url).netloc == urlparse(start_url).netloc:
            to_visit.append(full_url)
