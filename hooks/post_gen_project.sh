#!/usr/bin/env zsh
set -ueo pipefail

uv lock && git init && git add . \
    && git commit --message '{{ cookiecutter.description }}' \
                  --message 'Bootstrapped from https://github.com/r73m/cookiecutter-python-app'

{% if cookiecutter.github in [True, 'y'] %}
gh repo create --private --source . --push \
  --description '{{ cookiecutter.description }}'
gh repo edit \
  --enable-merge-commit=false \
  --enable-rebase-merge=false \
  --delete-branch-on-merge \
  --allow-update-branch
{% endif %}
