PYTHON ?= python3

.PHONY: update-public update-private render-private render-public check

update-public:
	$(PYTHON) scripts/update_metadata.py
	$(PYTHON) scripts/render_docs.py --public

update-private:
	$(PYTHON) scripts/update_metadata.py
	$(PYTHON) scripts/render_docs.py

render-public:
	$(PYTHON) scripts/render_docs.py --public

render-private:
	$(PYTHON) scripts/render_docs.py --private

check:
	$(PYTHON) -m unittest discover -s tests
	$(PYTHON) scripts/check_links.py
