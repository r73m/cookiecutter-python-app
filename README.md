# My Python CLI app template
This repository contains a [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for creating installable[^1] command-line Python applications with configured essential developer tooling: [uv](https://docs.astral.sh/uv), [Ruff](https://docs.astral.sh/ruff), [ty](https://docs.astral.sh/ty), [pytest](https://pytest.org), [Make](https://www.gnu.org/software/make), [Dependabot](https://docs.github.com/en/code-security/dependabot), and [GitHub Actions](https://github.com/features/actions).
## How to use?
```shell
uvx cookiecutter gh:r73m/cookiecutter-python-app
```
[^1]: The main targeted use case is installation from a private GitHub repository with a command like `uv tool install git+ssh://git@github.com/{user}/{repo}.git`.
