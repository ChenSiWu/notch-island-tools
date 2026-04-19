# Contributing

This repository tracks Mac notch / Dynamic Island tools and AI coding island tools.

## Public data

- `data/tools.json`: public tool catalog used to generate `README.md`
- `data/generated-metadata.json`: generated GitHub/link metadata for the public repo

## Private local data

- `data/local-notes.json` is local-only and ignored by git
- `PRIVATE.md` is generated locally and ignored by git

## Useful commands

```bash
python3 -m unittest discover -s tests
python3 scripts/check_links.py
python3 scripts/update_metadata.py
python3 scripts/render_docs.py --public
make update-public
make update-private
```

## Automation

- GitHub Actions updates public metadata and `README.md` weekly
- Local private notes should be maintained separately from public data
