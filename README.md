# Mac 刘海屏 / 灵动岛工具对比

更新时间：2026-04-19

这份文档分成两大类：通用刘海屏 / 灵动岛工具，以及 AI Coding / Vibe Coding 刘海屏工具。

## 当前结论

通用工具继续以 **Atoll** 为主力，**BoringNotch** 做开源备用。AI Coding 工具优先试 **CodeIsland** 和 **Open Island**；重度 Claude Code 再看 **MioIsland / Claude Island / Notchi**。

## Quick Start

如果你只是查看工具对比，直接阅读这份 `README.md` 就可以。

如果你想在本地维护自己的私有体验层：

1. 复制 `data/local-notes.example.json` 为 `data/local-notes.json`
2. 按自己的机器情况填写本地安装包、验证结果和主力工具
3. 执行 `make update-private` 生成本地 `PRIVATE.md`

`PRIVATE.md` 和 `data/local-notes.json` 默认不会进入公开仓库。

## 状态说明

| 状态 | 含义 |
| --- | --- |
| 推荐 | 地址和下载入口清楚，仍在更新，功能与当前需求匹配，适合优先试 |
| 可试 | 地址可用，但功能偏单一、闭源信息有限、或需要按场景验证 |
| 观察 | 项目还早、热度低、Release 不完整、版本信息不一致，先记录不主用 |
| 过时/归档/谨慎 | 官网/下载不可用、很久没更新、下载链路不可信，或本质不是灵动岛工具 |

## 系统要求速查

这部分保留兼容性信息。版本要求以后可能变化，安装前仍以官网 / Release / App Store / Setapp 页面为准。

| 工具 | 系统要求 / 兼容性记录 |
| --- | --- |
| Atoll | 之前记录为 macOS 14+，更适合 macOS 15+ |
| BoringNotch | 之前记录为 macOS 14+，Apple Silicon / Intel 均可关注 |
| NookX | App Store 工具，之前记录为 macOS 13+ |
| NotchNook | 之前记录为 macOS 14.6+ |
| Alcove | Homebrew Cask 显示 macOS 14+ |
| MacNotch | Setapp 页面显示 macOS 14+ |
| LookieLoo | 官网 / App Store 方向记录为 macOS 15+ |
| Notchable | 官网方向记录为 macOS 15+ |
| Notchpad | 官网显示 macOS 14+ |
| MioIsland | 之前记录为 macOS 15+ |
| Vibe Island | Homebrew Cask 显示 macOS 14+ |
| Notchi | 官网 / Release 方向要求 macOS Sequoia |
| Notchy | GitHub README 方向记录为 macOS 26.0+，因此只放观察区 |

# 一、通用刘海屏 / 灵动岛工具

## 通用工具总表

| 排名 | 工具 | 状态 | GitHub Stars | 更新/热度/反馈 | 地址 | 官方功能范围与我的判断 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Atoll | 推荐，开源 | 1.7k+ | Release v2.1.0，2026-03-21；仓库 2026-04 仍活跃 | [GitHub](https://github.com/Ebullioscopic/Atoll) / [Release](https://github.com/Ebullioscopic/Atoll/releases/latest) | 官方写明支持 Apple Music、Spotify 等媒体控制，还包括系统状态、Live Activities、锁屏小组件、文件 Shelf、剪贴板、日历、计时器。当前最适合当主力 |
| 2 | BoringNotch | 推荐，开源 | 8.4k+ | Release v2.7.3，2025-11-24；社区热度最高 | [官网](https://boringnotch.com/) / [GitHub](https://github.com/TheBoredTeam/boring.notch) / [Release](https://github.com/TheBoredTeam/boring.notch/releases/latest) | 官网强调媒体控制、文件 Shelf、日历、镜子、电池、HUD 替换。功能没有 Atoll 满，但作为开源备用很稳 |
| 3 | Alcove | 推荐，闭源商业 | 无 | Homebrew Cask 1.7.2；近 365 天约 3k+ 安装；官网和下载页可用 | [官网](https://tryalcove.com/) / [下载页](https://tryalcove.com/download) | 主打通知、Live Activities、HUD、滑动手势、锁屏小组件和原生动画。适合想买一个手感好的商业工具 |
| 4 | LookieLoo | 可试，闭源商业 | 无 | 官网和 App Store 可用；定位清楚 | [官网](https://lookielooapp.org/) / [App Store](https://apps.apple.com/us/app/lookieloo-rock-your-notch/id6747730721?mt=12) | 官方明确支持 Spotify、Apple Music、Chrome/Safari 里的 YouTube 和 YouTube Music，同步歌词、文件托盘、AirDrop、剪贴板历史。适合音乐 + 文件托盘场景 |
| 5 | MacNotch | 可试，闭源商业 | 无 | Setapp 版本 1.8.4.2；Setapp 信息完整 | [Setapp](https://setapp.com/apps/macnotch) | Setapp 写明支持 Spotify、Apple Music、YouTube、浏览器播放器，还包含任务、事件、计时器、小组件、设备电量、文件 Drop、HUD、OpenAI/Ollama 翻译。Setapp 用户值得试 |
| 6 | DynamicLake | 可试，闭源商业 | 无 | 官网可用；功能很多，但版本/下载信息不够结构化 | [官网](https://www.dynamiclake.com/) | 官方写明 DynaMusic、DynaGlance、通知、来电、DynaDrop、DynaClip、计时器、蓝牙设备提醒、Liquid Glass。适合想试商业全家桶，但不建议优先买 |
| 7 | NookX | 可试，闭源 App Store | 无 | App Store 当前版本 2026.04.08，发布日期 2026-04-10 | [App Store](https://apps.apple.com/us/app/nook-x-%E6%95%88%E7%8E%87%E5%B2%9B-notch-%E7%95%AA%E8%8C%84%E9%92%9F-%E5%88%98%E6%B5%B7-todo/id6733240772?mt=12) | 中文效率岛，适合 Todo、番茄钟、天气、快捷启动、速记、展开动效。官方写第三方音乐 / Safari，实际音乐兼容性需要按播放器验证 |
| 8 | NotchNook | 可试，闭源商业 | 无 | Setapp 显示 1.5.5；官网可用；历史直链测试 404 | [官网](https://lo.cafe/notchnook) / [Setapp](https://setapp.com/apps/notchnook) | 官方/Setapp 描述包含媒体控制、日历事件、文件暂存/传输、摄像头预览。适合轻量成品体验，不建议唯一主力 |
| 9 | NotchDrop 新版 | 可试，闭源/问题仓库 | 无 | 官网可用，直接 DMG 可下载 | [官网](https://www.notchdrop.com/) / [DMG](https://cdn.notchdrop.com/NotchDrop-1.1.dmg) / [问题仓库](https://github.com/muhammadsaddamnur/notchdrop-issues/) | 从文件 Drop 扩展到剪贴板、音乐、AI Chat、AI Notes、录屏、摄像头、本地分享、Todo、命令快捷方式、截图标注。更像小工具合集 |
| 10 | Notchable | 可试，闭源商业 | 无 | 官网可用，DMG 可下载 | [官网](https://notchable.com/) / [DMG](https://files.notchable.com/Notchable.dmg) | 不是综合灵动岛，更像刘海里的 Todo / Focus：语音捕捉、AI 分类、番茄钟、日历和提醒同步 |
| 11 | Notchpad | 可试，闭源单功能 | 无 | 官网显示 v0.8.4，DMG 可下载 | [官网](https://www.notchpad.org/) / [DMG](https://qnxwrepfyxxmifel.public.blob.vercel-storage.com/Notchpad-0.8.4.dmg) | 刘海里的常驻记事本，支持打字/语音，本地存储。功能单一，但边界清楚 |

## 通用场景快速选择

| 需求 | 优先选择 | 备选 |
| --- | --- | --- |
| 一个工具尽量全覆盖 | Atoll | BoringNotch |
| 免费开源、用户多 | BoringNotch | Atoll |
| 音乐、歌词、YouTube / YouTube Music | LookieLoo | MacNotch、DynamicLake、Atoll |
| 文件暂存 / AirDrop / 拖拽 | Atoll、BoringNotch、LookieLoo | NotchDrop 新版、NotchNook |
| 顺滑动画和原生感 | Alcove | DynamicLake、NotchNook |
| 中文效率、Todo、番茄钟 | NookX | Notchable |
| Setapp 里顺手试 | MacNotch、NotchNook | 无 |

## 通用功能矩阵

| 功能 | Atoll | BoringNotch | Alcove | LookieLoo | MacNotch | DynamicLake | NookX | NotchNook | NotchDrop 新版 | Notchable | Notchpad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 音乐/媒体 | 官方：Apple Music、Spotify 等；第三方音乐需按环境验证 | 官方：媒体控制；第三方音乐需按环境验证 | 官方主打 Live Activities/HUD，媒体需实测 | 官方：Spotify、Apple Music、YouTube/YouTube Music、歌词 | 官方：Spotify、Apple Music、YouTube、浏览器播放器 | 官方：DynaMusic | 官方：第三方音乐/Safari；具体播放器需验证 | 官方：媒体控制；具体播放器需验证 | 官方：音乐控制 | 无 | 无 |
| 文件暂存/传输 | 有 Shelf | 有 Shelf | 未主打 | 有文件托盘 + AirDrop | 有文件 Drop | DynaDrop/DynaClip | 有文件暂存 | 有文件托盘/传输 | 强 | 无 | 无 |
| 日历/事件 | 有 | 有 | 有 | 不主打 | 有任务/事件 | DynaGlance | 有 | 有 | 不主打 | 有 | 无 |
| 待办/番茄钟 | 计时器 | 不主打 | 不主打 | 无 | 有任务/计时器 | 计时器 | 强 | 不主打 | Todo | 强 | 记录工具 |
| 系统状态/HUD | 系统状态强，含 CPU/GPU/内存/网络/磁盘 | 电池/HUD 等基础能力 | HUD 强 | 不主打 | 设备电量/HUD | 有设备/通知类能力 | 基础信息 | 基础 | 不主打 | 无 | 无 |
| 摄像头/镜子 | 需权限，按功能配置 | 有镜子 | 不主打 | 不主打 | 不主打 | 不主打 | 有镜子 | 有摄像头预览 | 有摄像头 | 无 | 无 |
| AI 功能 | 非核心 | 无 | 无 | 无 | OpenAI/Ollama 翻译 | 无 | 内置 AI 对话 | 无 | AI Chat/AI Notes | AI 整理任务 | 无 |

# 二、AI Coding / Vibe Coding 刘海屏工具

## AI Coding 工具总表

| 排名 | 工具 | 状态 | GitHub Stars | 更新/热度/反馈 | 地址 | 官方功能范围与我的判断 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | CodeIsland | 推荐，开源 MIT | 1k+ | Release v1.0.21，2026-04-16；中文 README 完整 | [GitHub](https://github.com/wxtsky/CodeIsland) / [Release](https://github.com/wxtsky/CodeIsland/releases/latest) | 支持 Claude Code、Codex、Gemini CLI、Cursor、Copilot、Trae、Qoder、Factory、CodeBuddy、OpenCode、Kimi Code CLI；像素风角色、自动 Hook、权限审批、问题回答、一键跳转 |
| 2 | Open Island | 推荐，开源 GPL-3.0 | 580+ | Release v1.0.25，2026-04-18；仓库活跃 | [GitHub](https://github.com/Octane0411/open-vibe-island) / [Release](https://github.com/Octane0411/open-vibe-island/releases/latest) | 开源、local-first、无账号无遥测，Agent 和终端/IDE 覆盖很广。适合和 CodeIsland 做同场景对比 |
| 3 | MioIsland | 推荐，开源非商业许可 | 330+ | Release v2.1.7，2026-04-18；仓库活跃 | [GitHub](https://github.com/MioMioOS/MioIsland) / [Release](https://github.com/MioMioOS/MioIsland/releases/latest) | Claude Code 深度体验强：像素猫、/buddy、刘海审批、AskUserQuestion、Codex、iPhone Code Light、插件市场、Stats/Music 插件 |
| 4 | Vibe Island | 推荐，闭源商业 | 无 | Homebrew Cask 1.0.27；官网信息完整 | [官网](https://vibeisland.app/) / [下载页](https://vibeisland.app/download) | 商业化完整体验：零配置、GUI 审批、问题回答、Plan Review、用量追踪、SSH Remote、13+ 终端、纯 Swift。开源方案不稳时考虑 |
| 5 | Claude Island | 推荐，开源 Apache-2.0 | 2.1k+ | Release v1.3.1，2026-04-15；Claude 专用热度高 | [官网](https://claudeisland.com/) / [GitHub](https://github.com/farouqaldori/claude-island) / [Release](https://github.com/farouqaldori/claude-island/releases/latest) | Claude Code 专用，权限提醒、实时监控、多会话、聊天历史、SwiftUI 原生 |
| 6 | xisland | 推荐/可试，免费 | 源码入口未确认 | 官网显示 v0.2.0；Homebrew 安装明确 | [官网](https://xisland.app/) | 免费、Swift 原生，支持 Claude Code、Codex、Gemini CLI、OpenCode；有 Notch/Pill 模式、审批、回答、终端跳转、键盘优先 |
| 7 | Notchi | 可试，开源 GPL-3.0 | 770+ | Release v1.0.5，2026-04-09；仓库活跃 | [官网](https://notchi.app/) / [GitHub](https://github.com/sk-ruban/notchi) / [DMG](https://github.com/sk-ruban/notchi/releases/download/v1.0.5/Notchi-1.0.5.dmg) | Claude Code companion，实时响应 thought、tool call、error；要求 macOS Sequoia |
| 8 | Clautch | 可试，源码可见 | 0 | Release v0.27.0，2026-04-18；仓库很新 | [官网](https://clautch.app/) / [GitHub](https://github.com/sophiie-ai/clautch) / [Release](https://github.com/sophiie-ai/clautch/releases/latest) | Claude Code 状态宠物，带团队房间、聊天、像素反应和等待输入提醒，更偏陪伴和团队氛围 |
| 9 | NotchCode | 可试，闭源商业 | 无 | 官网可用，闭源商业 | [官网](https://notchcode.dev/) | 支持 Claude Code、Gemini CLI、Codex；实时监控、Inline Approval、聊天历史、智能通知，依赖 tmux 管理会话 |
| 10 | Ping Island | 观察，开源 Apache-2.0 | 140+ | Release v0.3.0，2026-04-18；仓库活跃但项目早期 | [主页](https://erha19.github.io/ping-island) / [GitHub](https://github.com/erha19/ping-island) / [Release](https://github.com/erha19/ping-island/releases/latest) | Vibe Island 风格，支持审批、追问、窗口跳转，适合作为开源替代观察 |
| 11 | Notch Pilot | 观察，开源 MIT | 30+ | Release v0.4.8，2026-04-17；项目很新 | [GitHub](https://github.com/devmegablaster/Notch-Pilot) / [Release](https://github.com/devmegablaster/Notch-Pilot/releases/latest) | Claude 用量、会话状态、权限提示、动画 buddy；先观察稳定性 |
| 12 | Tars Notch | 观察，开源 MIT | 3 | Release v2.0.0，2026-03-31；热度低 | [GitHub](https://github.com/ohernandezdev/tars-notch) / [Release](https://github.com/ohernandezdev/tars-notch/releases/latest) | 支持 Claude Code 和 GitHub Copilot CLI；多会话状态、权限审批、模型/模式、subagent 状态、本地 HTTP 服务 |

## AI Coding 场景快速选择

| 需求 | 优先选择 | 备选 |
| --- | --- | --- |
| 开源、多 Agent 覆盖 | CodeIsland | Open Island |
| local-first、终端/IDE 覆盖广 | Open Island | CodeIsland |
| Claude Code 深度体验 | MioIsland | Claude Island、Notchi |
| Codex 监控 | CodeIsland、Open Island | MioIsland、Vibe Island、xisland |
| 省心商业方案 | Vibe Island | NotchCode |
| 免费轻量 | xisland | CodeIsland |
| iPhone 联动 | MioIsland | 无 |

## AI Coding 功能矩阵

| 功能 | CodeIsland | Open Island | MioIsland | Vibe Island | Claude Island | xisland | Notchi | Clautch | NotchCode | Ping Island | Notch Pilot | Tars Notch |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Claude Code | 强 | 强 | 强 | 强 | 强 | 强 | 强 | 强 | 强 | 有 | 有 | 有 |
| Codex | 有，基础支持 | 强 | 有 | 强 | 无 | 有 | 无 | 无 | 有 | 待确认 | 无 | 无 |
| Gemini CLI | 有 | 强 | 未主打 | 强 | 无 | 有 | 无 | 无 | 有 | 待确认 | 无 | 无 |
| Cursor / IDE Agent | 有 | 强 | 激活/跳转为主 | 强 | 无 | 有 | 无 | 无 | 无 | 待确认 | 无 | 无 |
| OpenCode | 有 | 强 | 未主打 | 强 | 无 | 有 | 无 | 无 | 无 | 待确认 | 无 | 无 |
| 权限审批 | 有 | 有 | 强 | 强 | 有 | 有 | 状态为主 | 提醒为主 | 有 | 有 | 提醒为主 | 有 |
| Agent 问题回答 | 有 | 有 | 有 | 有 | 未主打 | 有 | 未主打 | 未主打 | 未主打 | 有 | 未主打 | 未主打 |
| 终端跳转 | 有 | 强 | cmux/iTerm/Ghostty/Terminal 等 | 强，含 13+ 终端 | 有 | 有 | 未主打 | 未主打 | tmux 方向 | 有 | 未主打 | 未主打 |
| 用量/额度显示 | 未主打 | 有 | 有 | 有 | 未主打 | 有 | 未主打 | 有 | 未主打 | 待确认 | 有 | 未主打 |
| iPhone 联动 | 无 | 无 | 强，Code Light | 无 | 无 | 无 | 无 | 无 | 无 | 无 | 无 | 无 |
| 插件生态 | 无 | 无 | 有插件市场 | 声音包/商业扩展 | 无 | 未主打 | 无 | 无 | 无 | 无 | 无 | 无 |

# 三、观察、过时与安全规则

## 观察 / 过时 / 归档 / 谨慎列表

| 工具 | 分类 | GitHub Stars | 更新/状态 | 地址 | 保留原因 |
| --- | --- | --- | --- | --- | --- |
| NotchDrop 原版 | 观察，开源 MIT | 2k+ | 仓库 2026-01 仍有活动，但无正式 Release | [GitHub](https://github.com/Lakr233/NotchDrop) | 原版专注文件暂存和 AirDrop，思路干净，但安装入口不够清晰 |
| OpenNotch | 观察，开源情况不明 | 0 | 仓库 2025-11 后未见 Release | [官网](https://www.opennotch.com/) / [GitHub](https://github.com/NikitaStogniy/OpenNotch) | 文件 Drop、计算器、快速访问，功能轻，但热度很低 |
| NotchBar | 观察，开源 AGPL-3.0 | 120+ | 仓库 2025-12 活跃；官网写 1.5.4，但 GitHub 最新公开 Release 是 2025-01 prerelease | [官网](https://deepak-kumar.github.io/NotchBar-Distribution/) / [GitHub](https://github.com/navtoj/NotchBar) | 媒体、系统状态、文件托盘、截图/录屏、全局热键，像开源控制中心，但版本信息不一致 |
| MediaMate | 归档/边界类 | 无 | 官网可访问，页面版权停在 2024 | [官网](https://wouter01.github.io/MediaMate/) | 更像媒体/HUD 工具，不是完整灵动岛 |
| Notchy | 观察，开源 MIT | 660+ | 仓库 2026-03 活跃，但无 Release，要求 macOS 26.0+ | [GitHub](https://github.com/adamlyttleapps/notchy) | Xcode + Claude 的内嵌终端面板，需要源码构建 |
| VNOCH | 过时/不可用 | 无 | 官网和下载页测试 404 | [原官网](https://www.vnoch.app/) | 保留记录，不作为当前候选 |
| NotchPro | 过时/不可用 | 无 | 官网 SSL 访问失败 | [原官网](https://notchpro.app/) | 下载入口不可确认 |
| DynamicNotch | 过时/早期 Demo | 无 | 官网仍可访问，但显示早期 v0.0.0 - M1 Chip，插件/小组件仍是 coming soon | [官网](https://dynamic-notch.iamzachmoore.com/) | 早期 Demo，当前不建议试 |
| NotchHub | 谨慎 | 无 | 官网可访问，但下载指向 mediafireupload.xyz/Launcher.dmg | [官网](https://notchhub.pro/) | 下载链路不可信，先不要装 |
| Notchmeister | 归档/娱乐 | 无 | 原 Iconfactory 链接测试 404 | [原说明](https://blog.iconfactory.com/2021/11/notchmeister/) | 趣味玩具，不是生产力工具 |
| TopNotch | 归档/边界类 | 无 | 官网可访问 | [官网](https://topnotch.app/) | 用来隐藏刘海，不是灵动岛 |
| Notched Up | 归档/测试工具 | 无 | 官网可访问 | [官网](https://ohanaware.com/notchedup/) | 模拟刘海，方便测试和截图 |
| Notch | 归档/同名无关 | 无 | 官网可访问 | [官网](https://www.notch.sh/) | 名字相似，但实际是开发者笔记本 |

## 安全和下载规则

- 只从官网、GitHub 主仓库、GitHub Releases、Mac App Store、Setapp、Homebrew 官方 cask 安装。
- 如果下载页要求把文件拖进 Terminal 执行，或者要求输入管理员密码，先不要装。
- DynamicLake 只从 `dynamiclake.com` 获取，不要用相似域名。
- NotchHub 当前不建议下载，因为下载链路跳到第三方文件站。
- AI Coding 工具安装后，要记录它改了哪些 Hook 配置。
- 同一时间只开一个通用刘海屏工具，避免多个工具抢同一块刘海区域。

## 参考链接总索引

### 通用刘海屏 / 灵动岛

- [Atoll GitHub](https://github.com/Ebullioscopic/Atoll)
- [Atoll Release](https://github.com/Ebullioscopic/Atoll/releases/latest)
- [BoringNotch 官网](https://boringnotch.com/)
- [BoringNotch GitHub](https://github.com/TheBoredTeam/boring.notch)
- [BoringNotch Release](https://github.com/TheBoredTeam/boring.notch/releases/latest)
- [Alcove 官网](https://tryalcove.com/)
- [Alcove 下载页](https://tryalcove.com/download)
- [LookieLoo 官网](https://lookielooapp.org/)
- [LookieLoo App Store](https://apps.apple.com/us/app/lookieloo-rock-your-notch/id6747730721?mt=12)
- [MacNotch Setapp](https://setapp.com/apps/macnotch)
- [DynamicLake 官网](https://www.dynamiclake.com/)
- [NookX App Store](https://apps.apple.com/us/app/nook-x-%E6%95%88%E7%8E%87%E5%B2%9B-notch-%E7%95%AA%E8%8C%84%E9%92%9F-%E5%88%98%E6%B5%B7-todo/id6733240772?mt=12)
- [NotchNook 官网](https://lo.cafe/notchnook)
- [NotchNook Setapp](https://setapp.com/apps/notchnook)
- [NotchDrop 新版 官网](https://www.notchdrop.com/)
- [NotchDrop 新版 DMG](https://cdn.notchdrop.com/NotchDrop-1.1.dmg)
- [NotchDrop 新版 问题仓库](https://github.com/muhammadsaddamnur/notchdrop-issues/)
- [Notchable 官网](https://notchable.com/)
- [Notchable DMG](https://files.notchable.com/Notchable.dmg)
- [Notchpad 官网](https://www.notchpad.org/)
- [Notchpad DMG](https://qnxwrepfyxxmifel.public.blob.vercel-storage.com/Notchpad-0.8.4.dmg)

### AI Coding / Vibe Coding

- [CodeIsland GitHub](https://github.com/wxtsky/CodeIsland)
- [CodeIsland Release](https://github.com/wxtsky/CodeIsland/releases/latest)
- [Open Island GitHub](https://github.com/Octane0411/open-vibe-island)
- [Open Island Release](https://github.com/Octane0411/open-vibe-island/releases/latest)
- [MioIsland GitHub](https://github.com/MioMioOS/MioIsland)
- [MioIsland Release](https://github.com/MioMioOS/MioIsland/releases/latest)
- [Vibe Island 官网](https://vibeisland.app/)
- [Vibe Island 下载页](https://vibeisland.app/download)
- [Claude Island 官网](https://claudeisland.com/)
- [Claude Island GitHub](https://github.com/farouqaldori/claude-island)
- [Claude Island Release](https://github.com/farouqaldori/claude-island/releases/latest)
- [xisland 官网](https://xisland.app/)
- [Notchi 官网](https://notchi.app/)
- [Notchi GitHub](https://github.com/sk-ruban/notchi)
- [Notchi DMG](https://github.com/sk-ruban/notchi/releases/download/v1.0.5/Notchi-1.0.5.dmg)
- [Clautch 官网](https://clautch.app/)
- [Clautch GitHub](https://github.com/sophiie-ai/clautch)
- [Clautch Release](https://github.com/sophiie-ai/clautch/releases/latest)
- [NotchCode 官网](https://notchcode.dev/)
- [Ping Island 主页](https://erha19.github.io/ping-island)
- [Ping Island GitHub](https://github.com/erha19/ping-island)
- [Ping Island Release](https://github.com/erha19/ping-island/releases/latest)
- [Notch Pilot GitHub](https://github.com/devmegablaster/Notch-Pilot)
- [Notch Pilot Release](https://github.com/devmegablaster/Notch-Pilot/releases/latest)
- [Tars Notch GitHub](https://github.com/ohernandezdev/tars-notch)
- [Tars Notch Release](https://github.com/ohernandezdev/tars-notch/releases/latest)

### 过时 / 归档 / 谨慎

- [NotchDrop 原版 GitHub](https://github.com/Lakr233/NotchDrop)
- [OpenNotch 官网](https://www.opennotch.com/)
- [OpenNotch GitHub](https://github.com/NikitaStogniy/OpenNotch)
- [NotchBar 官网](https://deepak-kumar.github.io/NotchBar-Distribution/)
- [NotchBar GitHub](https://github.com/navtoj/NotchBar)
- [MediaMate 官网](https://wouter01.github.io/MediaMate/)
- [Notchy GitHub](https://github.com/adamlyttleapps/notchy)
- [VNOCH 原官网](https://www.vnoch.app/)
- [NotchPro 原官网](https://notchpro.app/)
- [DynamicNotch 官网](https://dynamic-notch.iamzachmoore.com/)
- [NotchHub 官网](https://notchhub.pro/)
- [Notchmeister 原说明](https://blog.iconfactory.com/2021/11/notchmeister/)
- [TopNotch 官网](https://topnotch.app/)
- [Notched Up 官网](https://ohanaware.com/notchedup/)
- [Notch 官网](https://www.notch.sh/)
