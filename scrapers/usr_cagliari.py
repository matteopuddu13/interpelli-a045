import requests
from bs4 import BeautifulSoup

URL = "https://www.mim.gov.it/web/cagliari/notizie"

def scrape():
    r = requests.get(URL, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")

    items = []

    for news in soup.select(".asset-summary"):
        title = news.get_text(" ", strip=True)
        link = news.find("a", href=True)

        if not link:
            continue

        items.append({
            "title": title,
            "content": title,
            "url": link["href"]
        })

    return items
