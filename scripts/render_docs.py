from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
STATUS_ROWS = [
    ["推荐", "地址和下载入口清楚，仍在更新，功能与当前需求匹配，适合优先试"],
    ["可试", "地址可用，但功能偏单一、闭源信息有限、或需要按场景验证"],
    ["观察", "项目还早、热度低、Release 不完整、版本信息不一致，先记录不主用"],
    ["过时/归档/谨慎", "官网/下载不可用、很久没更新、下载链路不可信，或本质不是灵动岛工具"],
]


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def link_list(links: list[dict[str, str]]) -> str:
    return " / ".join(f"[{item['label']}]({item['url']})" for item in links)


def table(headers: list[str], rows: list[list[str]]) -> str:
    output = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    output.extend("| " + " | ".join(row) + " |" for row in rows)
    return "\n".join(output)


def load_project_data(root: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    data_dir = root / "data"
    tools = load_json(data_dir / "tools.json", {"general": [], "ai_coding": [], "archived": []})
    local = load_json(data_dir / "local-notes.json", {})
    return tools, local


def render_tool_table(tools: list[dict[str, Any]]) -> str:
    rows: list[list[str]] = []
    for item in tools:
        rows.append(
            [
                str(item["rank"]),
                item["name"],
                item["status"],
                item.get("github_stars", "无"),
                item["metadata"],
                link_list(item["links"]),
                item["summary"],
            ]
        )
    return table(
        ["排名", "工具", "状态", "GitHub Stars", "更新/热度/反馈", "地址", "官方功能范围与我的判断"],
        rows,
    )


def render_feature_matrix(tools: list[dict[str, Any]], features: list[str]) -> str:
    headers = ["功能"] + [item["name"] for item in tools]
    rows: list[list[str]] = []
    for feature in features:
        rows.append([feature] + [item.get("features", {}).get(feature, "未主打") for item in tools])
    return table(headers, rows)


def render_quick_choices(choices: list[dict[str, str]]) -> str:
    return table(
        ["需求", "优先选择", "备选"],
        [[item["need"], item["primary"], item.get("backup", "无")] for item in choices],
    )


def render_reference_index(tools: dict[str, Any]) -> str:
    lines = ["## 参考链接总索引", "", "### 通用刘海屏 / 灵动岛", ""]
    for item in tools["general"]:
        for link in item["links"]:
            lines.append(f"- [{item['name']} {link['label']}]({link['url']})")
    lines.extend(["", "### AI Coding / Vibe Coding", ""])
    for item in tools["ai_coding"]:
        for link in item["links"]:
            lines.append(f"- [{item['name']} {link['label']}]({link['url']})")
    lines.extend(["", "### 过时 / 归档 / 谨慎", ""])
    for item in tools["archived"]:
        for link in item["links"]:
            lines.append(f"- [{item['name']} {link['label']}]({link['url']})")
    return "\n".join(lines)


def render_public(root: Path = ROOT) -> str:
    tools, _ = load_project_data(root)
    today = dt.date.today().isoformat()
    parts = [
        "# Mac 刘海屏 / 灵动岛工具对比",
        "",
        f"更新时间：{today}",
        "",
        "这份文档分成两大类：通用刘海屏 / 灵动岛工具，以及 AI Coding / Vibe Coding 刘海屏工具。",
        "",
        "## 当前结论",
        "",
        "通用工具继续以 **Atoll** 为主力，**BoringNotch** 做开源备用。AI Coding 工具优先试 **CodeIsland** 和 **Open Island**；重度 Claude Code 再看 **MioIsland / Claude Island / Notchi**。",
        "",
        "## 状态说明",
        "",
        table(["状态", "含义"], STATUS_ROWS),
        "",
        "## 系统要求速查",
        "",
        "这部分保留兼容性信息。版本要求以后可能变化，安装前仍以官网 / Release / App Store / Setapp 页面为准。",
        "",
        table(
            ["工具", "系统要求 / 兼容性记录"],
            [[item["tool"], item["note"]] for item in tools.get("system_requirements", [])],
        ),
        "",
        "# 一、通用刘海屏 / 灵动岛工具",
        "",
        "## 通用工具总表",
        "",
        render_tool_table(tools["general"]),
        "",
        "## 通用场景快速选择",
        "",
        render_quick_choices(tools.get("general_choices", [])),
        "",
        "## 通用功能矩阵",
        "",
        render_feature_matrix(tools.get("general", []), tools.get("general_features", [])),
        "",
        "# 二、AI Coding / Vibe Coding 刘海屏工具",
        "",
        "## AI Coding 工具总表",
        "",
        render_tool_table(tools.get("ai_coding", [])),
        "",
        "## AI Coding 场景快速选择",
        "",
        render_quick_choices(tools.get("ai_choices", [])),
        "",
        "## AI Coding 功能矩阵",
        "",
        render_feature_matrix(tools.get("ai_coding", []), tools.get("ai_features", [])),
        "",
        "# 三、观察、过时与安全规则",
        "",
        "## 观察 / 过时 / 归档 / 谨慎列表",
        "",
        render_archived_table(tools["archived"]),
        "",
        render_security_rules(),
        "",
        render_reference_index(tools),
        "",
    ]
    return "\n".join(parts)


def render_archived_table(items: list[dict[str, Any]]) -> str:
    rows = [
        [
            item["name"],
            item["category"],
            item.get("github_stars", "无"),
            item["metadata"],
            link_list(item["links"]),
            item["reason"],
        ]
        for item in items
    ]
    return table(["工具", "分类", "GitHub Stars", "更新/状态", "地址", "保留原因"], rows)


def render_private(root: Path = ROOT) -> str:
    tools, local = load_project_data(root)
    parts = [render_public(root).rstrip(), "", "# 私有本机记录", ""]
    installed = local.get("installed_packages", [])
    if installed:
        parts.extend(
            [
                "## 本地已有安装包",
                "",
                table(["工具", "本地文件", "当前角色"], [[i["tool"], i["file"], i["role"]] for i in installed]),
                "",
            ]
        )
    verification = local.get("verification", [])
    if verification:
        parts.extend(
            [
                "## 本机验证状态",
                "",
                table(
                    ["场景", "官方说明里的能力", "当前本机结论"],
                    [[i["scenario"], i["official"], i["local"]] for i in verification],
                ),
                "",
            ]
        )
    extra = local.get("extra_verification", [])
    if extra:
        parts.extend(
            [
                "## 本机补充验证项",
                "",
                table(["验证项", "为什么要测", "当前状态"], [[i["item"], i["why"], i["status"]] for i in extra]),
                "",
            ]
        )
    return "\n".join(parts)


def render_security_rules() -> str:
    return "\n".join(
        [
            "## 安全和下载规则",
            "",
            "- 只从官网、GitHub 主仓库、GitHub Releases、Mac App Store、Setapp、Homebrew 官方 cask 安装。",
            "- 如果下载页要求把文件拖进 Terminal 执行，或者要求输入管理员密码，先不要装。",
            "- DynamicLake 只从 `dynamiclake.com` 获取，不要用相似域名。",
            "- NotchHub 当前不建议下载，因为下载链路跳到第三方文件站。",
            "- AI Coding 工具安装后，要记录它改了哪些 Hook 配置。",
            "- 同一时间只开一个通用刘海屏工具，避免多个工具抢同一块刘海区域。",
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--public", action="store_true")
    parser.add_argument("--private", action="store_true")
    args = parser.parse_args()
    if not args.public and not args.private:
        args.public = True
        args.private = True
    if args.public:
        (args.root / "README.md").write_text(render_public(args.root), encoding="utf-8")
    if args.private:
        (args.root / "PRIVATE.md").write_text(render_private(args.root), encoding="utf-8")


if __name__ == "__main__":
    main()
