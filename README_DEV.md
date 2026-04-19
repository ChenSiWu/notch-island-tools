# notch-island-tools 开发说明

这个项目维护 Mac 刘海屏 / 灵动岛 / AI Coding 岛工具索引。

## 文件分工

- `data/tools.json`：公开工具数据，适合生成 `README.md`。
- `data/local-notes.json`：本机私有体验数据，默认被 `.gitignore` 忽略。
- `data/generated-metadata.json`：自动化生成的 GitHub / 链接状态数据，默认被 `.gitignore` 忽略。
- `README.md`：公开版，由脚本生成。
- `PRIVATE.md`：私有版，由脚本生成，默认被 `.gitignore` 忽略。

## 常用命令

```bash
python3 scripts/render_docs.py
python3 scripts/update_metadata.py
python3 scripts/check_links.py
python3 -m unittest discover -s tests
make update-private
```

## 自动化策略

- GitHub Actions：每周更新公开版 `README.md` 和 `data/generated-metadata.json`，并自动 commit + push。
  - 当前计划：每周一 `02:00 UTC`
  - 换算为中国时区：每周一 `10:00 Asia/Shanghai`
- 本机私有体验：继续由 `data/local-notes.json` 维护，不建议本机定时任务自动改写。
- 如果你直接告诉 Codex 新的体验结论，优先由 Codex 更新 `data/local-notes.json`，再重新生成 `PRIVATE.md`。

## 推荐本地用法

- 刷新公开数据并重生成公开/私有文档：

```bash
make update-private
```

- 只重生成文档，不拉新元数据：

```bash
make render-private
```
