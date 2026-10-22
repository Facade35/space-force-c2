"""Download the emblem files listed in manifest.csv from Wikimedia Commons.

Run from the repo root: python logos/fetch_logos.py
Skips files that already exist. Waits when Wikimedia asks it to slow down.
"""
import csv, os, time, urllib.error, urllib.request

UA = "SpaceForceC2LogoLibrary/1.0 (training reference; github.com/Facade35/space-force-c2)"
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

def fetch(url):
    for _ in range(20):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            return urllib.request.urlopen(req, timeout=60).read()
        except urllib.error.HTTPError as e:
            if e.code != 429:
                raise
            wait = int(e.headers.get("retry-after") or 30)
            print(f"  rate limited, waiting {wait}s")
            time.sleep(wait)
    raise RuntimeError("still rate limited: " + url)

with open(os.path.join(HERE, "manifest.csv"), encoding="utf-8") as f:
    for row in csv.DictReader(f):
        url, target = row["commons_original_url"], row["target_file"]
        if not url or not target:
            continue
        path = os.path.join(ROOT, target)
        if os.path.exists(path):
            continue
        print(target)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        data = fetch(url)
        with open(path, "wb") as out:
            out.write(data)
        time.sleep(2)
