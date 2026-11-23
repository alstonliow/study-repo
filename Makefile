PYTHON ?= python3

.PHONY: check readme test site pdf preview clean-site check-private site-private preview-private private-site-src

check:
	$(PYTHON) build/check.py

# Rewrite the statistics block in README.md (build/readme_stats.py)
readme:
	$(PYTHON) build/readme_stats.py

# Private build (SPEC §17.14): also reads private/. Local only; CI never runs these.
# Run check-private before committing either repository.
PRIVATE_SITE = out/private-site/src

check-private:
	STUDY_PRIVATE=1 $(PYTHON) build/check.py

# The private website: generated into out/private-site/src (never site/), rendered
# to out/private-site/src/_site, never deployed. The drawing cache is copied from site/.
private-site-src:
	rm -rf $(PRIVATE_SITE)
	mkdir -p $(PRIVATE_SITE)
	cp -R site/_quarto.yml site/_assets $(PRIVATE_SITE)/
	if [ -d site/tikz ]; then cp -R site/tikz $(PRIVATE_SITE)/; fi
	STUDY_PRIVATE=1 STUDY_SITE=$(PRIVATE_SITE) $(PYTHON) build/make_site.py

site-private: private-site-src
	quarto render $(PRIVATE_SITE)

preview-private: private-site-src
	quarto preview $(PRIVATE_SITE)

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
