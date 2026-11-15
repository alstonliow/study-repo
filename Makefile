PYTHON ?= python3

.PHONY: check test site preview clean-site

check:
	$(PYTHON) build/check.py

# Tests of the build scripts on tests/fixture (python3 tests/test_build.py --update
# accepts new expected output after an intended change)
test:
	$(PYTHON) tests/test_build.py

# Generate pages from notes/ and render the website into site/_site/
site:
	$(PYTHON) build/make_site.py
	quarto render site

# Live local preview (regenerates pages first)
preview:
	$(PYTHON) build/make_site.py
	quarto preview site

clean-site:
	rm -rf site/_site site/notes site/courses site/tikz site/index.qmd site/_nav.yml site/_sidebar.yml site/site-data.json site/.quarto
