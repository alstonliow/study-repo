PYTHON ?= python3

.PHONY: check

check:
	$(PYTHON) build/check.py
