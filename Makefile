PYTHON ?= python3

.PHONY: check test site pdf preview clean-site

check:
	$(PYTHON) build/check.py

# Tests of the build scripts on tests/fixture (python3 tests/test_build.py --update
# accepts new expected output after an intended change)
test:
	$(PYTHON) -m mypy
	$(PYTHON) tests/test_build.py

# Generate pages from notes/ and render the website into site/_site/
site:
	$(PYTHON) build/make_site.py
	quarto render site

# PDFs: the common versions (what the website offers) into out/pdf/.
# Other combinations: python3 build/make_pdf.py --help
pdf:
	$(PYTHON) build/make_pdf.py --all-presets

# Live local preview (regenerates pages first)
preview:
	$(PYTHON) build/make_site.py
	quarto preview site

# Remove everything generated in site/ (keeps _quarto.yml, _assets/ and .gitignore)
clean-site:
	find site -mindepth 1 -maxdepth 1 ! -name _quarto.yml ! -name _assets ! -name .gitignore -exec rm -rf {} +
