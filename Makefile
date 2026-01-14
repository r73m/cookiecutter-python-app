.SILENT:

ruff = uvx ruff
py_files = tests/*.py

.PHONY: prepare
prepare: format lint check-types test

.PHONY: format
format:
	$(ruff) format $(py_files)

.PHONY: lint
lint:
	$(ruff) check --fix $(py_files)

PHONY: test
test:
	tests/main.py

.PHONY: check-format
check-format:
	$(ruff) format --check $(py_files)

.PHONY: check-lint
check-lint:
	$(ruff) check $(py_files)

.PHONY: check-types
check-types:
	uvx ty check $(py_files)

.PHONY: clean
clean:
	rm -rf .DS_Store .ruff_cache

.PHONY: repo
repo:
	gh repo view --web
