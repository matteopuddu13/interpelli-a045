import os
from pathlib import Path
from scrapers.usr_cagliari import scrape as scrape_usr
from scrapers.usp_cagliari import scrape as scrape_usp
from services.detector import is_a045
from services.notifier import notify

SEEN_FILE = Path("seen.txt")

seen = set(SEEN_FILE.read_text().splitlines()) if SEEN_FILE.exists() else set()
new_seen = set()

sources = [scrape_usr, scrape_usp]

for scrape in sources:
    try:
        items = scrape()
    except Exception as e:
        print(f"[WARN] errore nello scraper {scrape.__name__}: {e}")
        continue

    for item in items:
        url = item["url"].strip()
        text = (item["title"] + " " + item["content"]).lower()

        if url in seen:
            continue

        new_seen.add(url)

        if is_a045(text):
            notify(item)

if new_seen:
    SEEN_FILE.write_text("\n".join(sorted(seen | new_seen)))
