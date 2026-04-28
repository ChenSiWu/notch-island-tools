from __future__ import annotations

import datetime as dt
import json
import os
import re
import subprocess
import urllib.error
import urllib.request
from functools import lru_cache
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
HEADERS = {"User-Agent": "notch-island-tools metadata updater"}

# This script only collects public, objective metadata:
# GitHub repo metadata and link status. Local/private experience notes live in
# data/local-notes.json and are intentionally not read or modified here.


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


@lru_cache(maxsize=1)
def github_auth_token() -> str | None:
    for env_name in ("GITHUB_TOKEN", "GH_TOKEN"):
        token = os.environ.get(env_name)
        if token:
            return token
    try:
        result = subprocess.run(
            ["gh", "auth", "token"],
            check=True,
            capture_output=True,
            text=True,
        )
        token = result.stdout.strip()
        return token or None
    except Exception:
        return None


def fetch_json(url: str) -> dict[str, Any]:
    headers = {**HEADERS, "Accept": "application/vnd.github+json"}
    token = github_auth_token()
    if token and "api.github.com" in url:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
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


def extract_app_store_id(url: str) -> str | None:
    match = re.search(r"/id(\d+)", url)
    return match.group(1) if match else None


def app_store_metadata(app_id: str) -> dict[str, Any] | None:
    lookup_url = f"https://itunes.apple.com/lookup?id={app_id}&country=us"
    try:
        data = fetch_json(lookup_url)
    except Exception:
        return None
    results = data.get("results") or []
    if not results:
        return None
    item = results[0]
    return {
        "version": item.get("version"),
        "release_date": (item.get("currentVersionReleaseDate") or "")[:10],
        "track_url": item.get("trackViewUrl"),
        "track_name": item.get("trackName"),
    }


def homebrew_metadata(cask: str) -> dict[str, Any] | None:
    try:
        result = subprocess.run(
            ["brew", "info", "--cask", "--json=v2", cask],
            check=True,
            capture_output=True,
            text=True,
        )
        data = json.loads(result.stdout)
    except Exception:
        return None
    casks = data.get("casks") or []
    if not casks:
        return None
    item = casks[0]
    return {
        "version": item.get("version"),
        "homepage": item.get("homepage"),
        "token": item.get("token"),
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
            app_store_id = tool.get("app_store_id")
            if app_store_id:
                app_store = app_store_metadata(app_store_id)
                if app_store:
                    item["app_store"] = app_store
            cask = tool.get("homebrew_cask")
            if cask:
                brew = homebrew_metadata(cask)
                if brew:
                    item["homebrew"] = brew
            for link in tool.get("links", []):
                item["links"][link["label"]] = check_url(link["url"])
            metadata["tools"][tool["name"]] = item
    return metadata


def main() -> None:
    # The generated file is public and safe to commit. It should never include
    # installed packages, machine-specific test results, or personal notes.
    output = ROOT / "data" / "generated-metadata.json"
    output.write_text(json.dumps(collect(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
