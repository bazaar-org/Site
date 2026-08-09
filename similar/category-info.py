import argparse
import gzip
import json
import time
import sys
import urllib.request
import urllib.error
import urllib.parse
from pathlib import Path

BASE_URL = "https://flathub.org/api/v2"
ADWAITA_URL = "https://arewelibadwaitayet.com/api/apps"
PER_PAGE = 1000
QUALITY_PAGE_SIZE = 1000
REQUEST_DELAY = 0.2

COLLECTIONS = {
    "/collection/popular": "popular",
    "/collection/trending": "trending",
    "/collection/recently-updated": "recently_updated",
    "/collection/recently-added": "recently_added",
}

BOOL_FIELDS = ["quality_passing", "kde", "gnome"]


def http_get_json(url: str, params: dict | None = None, timeout: int = 30) -> dict:
    if params:
        url = f"{url}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": "Bazaar Site fetcher"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        charset = resp.headers.get_content_charset() or "utf-8"
        body = resp.read().decode(charset)
    return json.loads(body)


def fetch_collection(path: str) -> list[dict]:
    hits = []
    page = 1
    data = {}
    while True:
        data = http_get_json(
            f"{BASE_URL}{path}",
            params={"page": page, "per_page": PER_PAGE},
            timeout=30,
        )
        page_hits = data.get("hits", [])
        hits.extend(page_hits)
        total_hits = data.get("totalHits", len(hits))
        total_pages = data.get("totalPages", page)
        print(
            f"  {path}: page {page}/{total_pages} "
            f"({len(hits)}/{total_hits} apps so far)"
        )
        if page >= total_pages or not page_hits:
            break
        page += 1
        time.sleep(REQUEST_DELAY)
    return hits


def fetch_quality_passing_ids() -> set[str]:
    ids: set[str] = set()
    page = 1
    while True:
        data = http_get_json(
            f"{BASE_URL}/quality-moderation/passing-apps",
            params={"page": page, "page_size": QUALITY_PAGE_SIZE},
            timeout=30,
        )
        apps = data.get("apps", [])
        ids.update(apps)
        print(f"  quality-moderation: page {page} ({len(ids)} apps so far)")
        if len(apps) < QUALITY_PAGE_SIZE:
            break
        page += 1
        time.sleep(REQUEST_DELAY)
    return ids


def fetch_kde_ids() -> set[str]:
    hits = fetch_collection("/collection/developer/kde")
    return {app.get("app_id") or app.get("id") for app in hits if app.get("app_id") or app.get("id")}


def fetch_gnome_ids() -> set[str]:
    data = http_get_json(ADWAITA_URL, timeout=30)
    if isinstance(data, dict):
        return set(data.keys())
    return set()


def build_merged_index() -> dict:
    merged: dict[str, dict] = {}

    def get_entry(app_id: str) -> dict:
        return merged.setdefault(
            app_id,
            {
                **{k: None for k in COLLECTIONS.values()},
                **{k: False for k in BOOL_FIELDS},
            },
        )

    for path, key in COLLECTIONS.items():
        print(f"Fetching {key} ...")
        hits = fetch_collection(path)
        for rank, app in enumerate(hits, start=1):
            app_id = app.get("app_id") or app.get("id")
            if not app_id:
                continue
            entry = get_entry(app_id)
            entry[key] = rank
        time.sleep(REQUEST_DELAY)

    print("Fetching quality")
    for app_id in fetch_quality_passing_ids():
        get_entry(app_id)["quality_passing"] = True
    time.sleep(REQUEST_DELAY)

    print("Fetching KDE apps")
    for app_id in fetch_kde_ids():
        get_entry(app_id)["kde"] = True
    time.sleep(REQUEST_DELAY)

    print("Fetching Adwaita")
    for app_id in fetch_gnome_ids():
        get_entry(app_id)["gnome"] = True

    return merged


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output-folder",
        default="collection-data",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    merged = build_merged_index()
    sorted_merged = {app_id: merged[app_id] for app_id in sorted(merged)}
    payload = json.dumps(sorted_merged, indent=2, ensure_ascii=False)
    out_path = Path(args.output_folder)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(out_path, "wt", encoding="utf-8") as f:
        f.write(payload)
    print(f"\nWrote {len(sorted_merged)} apps to {out_path.resolve()}")


if __name__ == "__main__":
    try:
        main()
    except urllib.error.URLError as e:
        print(f"Request failed: {e}", file=sys.stderr)
        sys.exit(1)
