#!/usr/bin/env python3
"""Download all 72 cars.com images and map them to local files."""
import csv, urllib.request, os, sys
from concurrent.futures import ThreadPoolExecutor

# Map entity → local id
ID_MAP = {
    "2024 Ford Bronco Raptor Certified Pre-Owned blue": "bronco-raptor-cert-blue",
    "2026 Jeep Wrangler Unlimited Sport S": "wrangler-sport-s",
    "2026 BMW 228i Gran Coupe xDrive": "bmw-228-gran-coupe",
    "2026 Ford Mustang EcoBoost Convertible Premium light blue": "mustang-conv-light-blue",
    "2026 MINI Cooper S 4 door pink": "mini-cooper-4door-pink",
    "2026 Toyota Land Cruiser 1958": "landcruiser-1958",
    "2026 GMC Yukon Denali 6.2": "yukon-denali",
    "2026 Cadillac Escalade Sport V8": "escalade-sport",
    "2024 Jeep Wrangler Rubicon 4 door Certified Pre-Owned": "wrangler-rubicon-cert",
}

ROOT = "/home/user/workspace/site-number-1/images/gallery"
os.makedirs(ROOT, exist_ok=True)

def download(args):
    url, path = args
    if os.path.exists(path) and os.path.getsize(path) > 5000:
        return f"SKIP {path}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as r:
            data = r.read()
        with open(path, 'wb') as f:
            f.write(data)
        return f"OK {os.path.basename(path)} ({len(data)//1024}KB)"
    except Exception as e:
        return f"FAIL {url[:60]}: {e}"

tasks = []
with open("/home/user/workspace/site-number-1/cars_v6_images.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        car_id = ID_MAP.get(row["entity"])
        if not car_id:
            print(f"UNKNOWN: {row['entity']}")
            continue
        for i in range(1, 9):
            url = row.get(f"Image {i}", "").strip()
            if url:
                ext = ".jpg"
                path = os.path.join(ROOT, f"{car_id}-{i}{ext}")
                tasks.append((url, path))

print(f"Downloading {len(tasks)} images...")
with ThreadPoolExecutor(max_workers=10) as ex:
    for r in ex.map(download, tasks):
        print(r)
