from __future__ import annotations

import datetime as dt
import json
import os
import re
import subprocess
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[1]
HEADERS = {"User-Agent": "notch-island-tools metadata updater"}

# This script only collects public, objective metadata:
# GitHub, App Store, Homebrew, Setapp, configured website versions, and link
# status. Local/private experience notes live in data/local-notes.json and are
# intentionally not read or modified here.


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


def stable_final_url(original_url: str, final_url: str) -> str:
    # GitHub release assets redirect to short-lived signed URLs. Keeping the
    # original URL avoids noisy metadata diffs on every scheduled run.
    if "release-assets.githubusercontent.com" in final_url:
        return original_url
    return final_url


def check_url(url: str) -> dict[str, Any]:
    req = urllib.request.Request(url, headers=HEADERS, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=20) as response:
            return {"status": response.status, "final_url": stable_final_url(url, response.geturl())}
    except urllib.error.HTTPError as exc:
        return {"status": exc.code, "final_url": stable_final_url(url, exc.geturl())}
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


def fetch_text(url: str) -> str | None:
    headers = {**HEADERS, "Accept": "text/html,application/xhtml+xml"}
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=20) as response:
            return response.read().decode("utf-8", "ignore")
    except Exception:
        return None


def website_version_metadata(
    config: dict[str, Any],
    fetcher: Callable[[str], str | None] = fetch_text,
) -> dict[str, Any] | None:
    url = config.get("url")
    pattern = config.get("pattern")
    patterns = config.get("patterns") or ([pattern] if pattern else [])
    if not url or not patterns:
        return None

    text = fetcher(url)
    if not text:
        return None

    flags = re.I if config.get("ignore_case", True) else 0
    for current_pattern in patterns:
        match = re.search(current_pattern, text, flags)
        if not match:
            continue

        group = config.get("group")
        if group is None:
            group = "version" if "version" in match.groupdict() else 1 if match.groups() else 0
        version = match.group(group).strip()
        return {
            "version": version,
            "label": config.get("label", "官网版本"),
            "source_url": url,
        }
    return None


def setapp_metadata(url: str) -> dict[str, Any] | None:
    html = fetch_text(url)
    if not html:
        return None
    match = re.search(r'Version":"([0-9.]+)"', html)
    if not match:
        match = re.search(r'Version\s+([0-9.]+)', html, re.I)
    if not match:
        return None
    return {"version": match.group(1)}


def collect_tool_metadata(group: str, tool: dict[str, Any]) -> tuple[str, dict[str, Any]]:
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
    setapp_url = tool.get("setapp_url")
    if setapp_url:
        setapp = setapp_metadata(setapp_url)
        if setapp:
            item["setapp"] = setapp
    website_version = tool.get("website_version")
    if website_version:
        website = website_version_metadata(website_version)
        if website:
            item["website_version"] = website
    for link in tool.get("links", []):
        link_status = check_url(link["url"])
        if link.get("allowed_statuses"):
            link_status["allowed_statuses"] = link["allowed_statuses"]
        item["links"][link["label"]] = link_status
    return tool["name"], item


def collect() -> dict[str, Any]:
    tools = load_json(ROOT / "data" / "tools.json", {})
    metadata: dict[str, Any] = {"updated_at": dt.datetime.now(dt.UTC).isoformat(), "tools": {}}
    jobs: list[tuple[str, dict[str, Any]]] = []
    for group in ("general", "ai_coding", "archived"):
        for tool in tools.get(group, []):
            jobs.append((group, tool))
    max_workers = min(len(jobs) or 1, int(os.environ.get("NOTCH_METADATA_WORKERS", "8")))
    # Futures are consumed in source order so generated JSON stays deterministic.
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(collect_tool_metadata, group, tool) for group, tool in jobs]
        for future in futures:
            name, item = future.result()
            metadata["tools"][name] = item
    return metadata


def main() -> None:
    # The generated file is public and safe to commit. It should never include
    # installed packages, machine-specific test results, or personal notes.
    output = ROOT / "data" / "generated-metadata.json"
    output.write_text(json.dumps(collect(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
