import requests
from bs4 import BeautifulSoup

URL = "https://www.uspcagliari.it/"

def scrape():
    r = requests.get(URL, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")

    items = []

    for a in soup.select("a"):
        text = a.get_text(" ", strip=True)
        href = a.get("href")

        if not href or len(text) < 10:
            continue

        items.append({
            "title": text,
            "content": text,
            "url": href
        })

    return items
