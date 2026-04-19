from __future__ import annotations

import datetime as dt
import json
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
HEADERS = {"User-Agent": "notch-island-tools metadata updater"}


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def fetch_json(url: str) -> dict[str, Any]:
    req = urllib.request.Request(url, headers={**HEADERS, "Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(req, timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))


def check_url(url: str) -> dict[str, Any]:
    req = urllib.request.Request(url, headers=HEADERS, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=20) as response:
            return {"status": response.status, "final_url": response.geturl()}
    except urllib.error.HTTPError as exc:
        return {"status": exc.code, "final_url": exc.geturl()}
    except Exception as exc:
        return {"status": "error", "error": str(exc)}


def github_metadata(repo: str) -> dict[str, Any]:
    info = fetch_json(f"https://api.github.com/repos/{repo}")
    latest_release = None
    try:
        latest = fetch_json(f"https://api.github.com/repos/{repo}/releases/latest")
        latest_release = {
            "tag": latest.get("tag_name"),
            "published_at": latest.get("published_at"),
            "url": latest.get("html_url"),
        }
    except Exception:
        latest_release = None
    return {
        "stars": info.get("stargazers_count"),
        "pushed_at": info.get("pushed_at"),
        "updated_at": info.get("updated_at"),
        "license": (info.get("license") or {}).get("spdx_id"),
        "archived": info.get("archived"),
        "latest_release": latest_release,
    }


def collect() -> dict[str, Any]:
    tools = load_json(ROOT / "data" / "tools.json", {})
    metadata: dict[str, Any] = {"updated_at": dt.datetime.now(dt.UTC).isoformat(), "tools": {}}
    for group in ("general", "ai_coding", "archived"):
        for tool in tools.get(group, []):
            item: dict[str, Any] = {"group": group, "links": {}}
            repo = tool.get("github_repo")
            if repo:
                try:
                    item["github"] = github_metadata(repo)
                except Exception as exc:
                    item["github_error"] = str(exc)
            for link in tool.get("links", []):
                item["links"][link["label"]] = check_url(link["url"])
            metadata["tools"][tool["name"]] = item
    return metadata


def main() -> None:
    output = ROOT / "data" / "generated-metadata.json"
    output.write_text(json.dumps(collect(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
