import argparse
import json
import os
from parser import fetch_apps
from similarity import find_similar_apps


def main(output_folder: str = "similar_apps", debug: bool = False):
    print("Fetching apps...")
    apps = fetch_apps()
    print(f"Fetched {len(apps)} apps")
    print("Computing similarity...")
    similar = find_similar_apps(apps, top_n=6)
    print("Similarity computation done")

    if debug:
        with open("similar_apps.json", "w", encoding="utf-8") as f:
            json.dump(similar, f, indent=2, ensure_ascii=False)
        print("Wrote similar_apps.json")

    os.makedirs(output_folder, exist_ok=True)
    for app_id, matches in similar.items():
        ids_only = [match_id for match_id, _ in matches]
        path = os.path.join(output_folder, app_id)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(ids_only, f, indent=2, ensure_ascii=False)

    print(f"Wrote {len(similar)} per-app files to {output_folder}/")

    return apps, similar


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-folder", default="similar_apps")
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()
    main(output_folder=args.output_folder, debug=args.debug)
