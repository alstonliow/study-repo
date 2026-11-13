PYTHON ?= python3

.PHONY: check site preview clean-site

check:
	$(PYTHON) build/check.py

# Generate pages from notes/ and render the website into site/_site/
site:
	$(PYTHON) build/make_site.py
	quarto render site

# Live local preview (regenerates pages first)
preview:
	$(PYTHON) build/make_site.py
	quarto preview site

clean-site:
	rm -rf site/_site site/notes site/courses site/tikz site/index.qmd site/_nav.yml site/_sidebar.yml site/courses.json site/.quarto
