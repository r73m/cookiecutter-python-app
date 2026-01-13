.SILENT:

uvx = uv run
ruff = $(uvx) ruff

.PHONY: prepare
prepare: format lint check-types test

.PHONY: format
format:
	$(ruff) format

.PHONY: lint
lint:
	$(ruff) check --fix

PHONY: test
test:
	$(uvx) pytest

.PHONY: check-format
check-format:
	$(ruff) format --check

.PHONY: check-lint
check-lint:
	$(ruff) check

.PHONY: check-types
check-types:
	$(uvx) ty check

.PHONY: clean
clean:
	rm -rf .coverage .venv dist

.PHONY: repo
repo:
	gh repo view --web
