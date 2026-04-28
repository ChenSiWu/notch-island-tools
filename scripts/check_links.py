from __future__ import annotations

import argparse

try:
    from update_metadata import collect
except ModuleNotFoundError:
    from scripts.update_metadata import collect


def is_link_failure(status: dict) -> bool:
    code = status.get("status")
    allowed = set(status.get("allowed_statuses", []))
    if code == "error":
        return True
    if isinstance(code, int) and code >= 400 and code not in allowed:
        return True
    return False


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
            if is_link_failure(status):
                failures.append(f"{tool} {label}: {status}")
    if failures:
        print("\n".join(failures))
        raise SystemExit(1)
    print("All links returned non-error status.")


if __name__ == "__main__":
    main()
