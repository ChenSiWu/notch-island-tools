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
```

