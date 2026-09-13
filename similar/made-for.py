import argparse
import json
import urllib.request
from pathlib import Path

from parser import fetch_apps

COSMIC_PROVIDES_ID = "com.system76.CosmicApplication"
ADWAITA_URL = "https://arewelibadwaitayet.com/api/apps"
KDE_URL = "https://flathub.org/api/v2/collection/developer/kde?locale=en"

HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) cosmic-similar-script"}


def fetch_json(url: str):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def fetch_cosmic_apps() -> list:
    apps = fetch_apps()
    return [app for app in apps if COSMIC_PROVIDES_ID in app.provides]


def fetch_adwaita_ids() -> list:
    data = fetch_json(ADWAITA_URL)
    return sorted(data.keys())


def fetch_kde_ids() -> list:
    data = fetch_json(KDE_URL)
    return sorted(hit["app_id"] for hit in data["hits"])


def write_ids(out_dir: Path, name: str, ids: list):
    payload = json.dumps(ids, indent=2)
    (out_dir / name).write_text(payload)
    print(f"Wrote {len(ids)} ids to {name}.json and {name}")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-folder", default=".")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    out_dir = Path(args.output_folder)
    out_dir.mkdir(parents=True, exist_ok=True)

    cosmic_apps = fetch_cosmic_apps()
    cosmic_ids = sorted(app.id for app in cosmic_apps)
    write_ids(out_dir, "cosmic", cosmic_ids)

    adwaita_ids = fetch_adwaita_ids()
    write_ids(out_dir, "adwaita", adwaita_ids)

    kde_ids = fetch_kde_ids()
    write_ids(out_dir, "kde", kde_ids)
