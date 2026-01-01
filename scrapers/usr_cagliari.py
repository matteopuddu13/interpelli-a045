import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE = "https://www.mim.gov.it"
URL = "https://www.mim.gov.it/web/cagliari/notizie"

def scrape():
    r = requests.get(URL, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")

    items = []

    for a in soup.select("a[href]"):
        text = a.get_text(" ", strip=True)
        href = a.get("href")

        if not text or "interpello" not in text.lower():
            continue

        full_url = urljoin(BASE, href)

        items.append({
            "title": text,
            "content": text,
            "url": full_url
        })

    return items
