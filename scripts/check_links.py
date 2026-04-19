from __future__ import annotations

import argparse

from update_metadata import collect


def main() -> None:
    parser = argparse.ArgumentParser()
    # Archived entries intentionally include broken or suspicious links.
    # They are useful historical records, so they should not fail the default
    # public link check unless explicitly requested.
    parser.add_argument("--include-archived", action="store_true")
    args = parser.parse_args()
    metadata = collect()
    failures: list[str] = []
    for tool, item in metadata["tools"].items():
        if not args.include_archived and item.get("group") == "archived":
            continue
        for label, status in item.get("links", {}).items():
            code = status.get("status")
            if code == "error" or (isinstance(code, int) and code >= 400):
                failures.append(f"{tool} {label}: {status}")
    if failures:
        print("\n".join(failures))
        raise SystemExit(1)
    print("All links returned non-error status.")


if __name__ == "__main__":
    main()
