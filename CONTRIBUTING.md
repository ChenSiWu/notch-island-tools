# 参与维护

这个仓库用于维护 Mac 刘海屏 / 灵动岛工具，以及 AI Coding / Vibe Coding 刘海屏工具索引。

## 数据分工

- `data/tools.json`
  - 公开工具数据
  - 用来生成公开的 `README.md`

- `data/generated-metadata.json`
  - 自动化生成的 GitHub / 链接状态数据
  - 允许提交到公开仓库

- `data/local-notes.json`
  - 本地私有体验数据
  - 默认被 `.gitignore` 忽略，不进入公开仓库

- `README.md`
  - 公开版文档
  - 由脚本生成

- `PRIVATE.md`
  - 私有版文档
  - 由脚本生成
  - 默认被 `.gitignore` 忽略

- `LICENSE`
  - 当前使用 MIT License
  - 允许别人使用、修改、分发和再发布

## 常用命令

```bash
python3 -m unittest discover -s tests
python3 scripts/check_links.py
python3 scripts/update_metadata.py
python3 scripts/render_docs.py --public
make update-public
make update-private
```

## 自动化策略

- GitHub Actions：
  - 每周自动更新公开版 `README.md`
  - 每周自动更新 `data/generated-metadata.json`
  - 有变化时自动 commit + push
  - 只提交公开生成文件，不提交 `PRIVATE.md` 或 `data/local-notes.json`

- 本地私有体验：
  - 继续由 `data/local-notes.json` 维护
  - 不建议本机定时任务自动改写

## 建议维护方式

- 客观信息交给自动化更新：
  - GitHub stars
  - Release 信息
  - 链接状态
  - 公开 README

- 主观体验人工维护：
  - 哪个工具现在作为主力
  - 本机是否稳定
  - QQ 音乐、外接显示器、睡眠唤醒、权限范围等体验结论

- 如果只想本地刷新一次，可以执行：

```bash
make update-private
```
