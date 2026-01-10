import subprocess
from collections import OrderedDict
from typing import Any


def run(*commands):
    for command in commands:
        subprocess.run(command, check=True)


params: OrderedDict[str, Any] = {{ cookiecutter }}  # type: ignore  # noqa: F821  # fmt: skip

run(
    ["uv", "lock"],
    ["git", "init"],
    ["git", "add", "."],
    [
        "git", "commit",
        "--message", params["description"],
        "--message", "Bootstrapped from https://github.com/r73m/cookiecutter-python-app",
    ],
)  # fmt: skip

if params["github"] in [True, "y"]:
    run(
        [
            "gh", "repo", "create",
            "--private", "--push", "--source", ".",
            "--description", params["description"],
        ],
        [
            "gh", "repo", "edit",
            "--enable-merge-commit=false",
            "--enable-rebase-merge=false",
            "--delete-branch-on-merge",
            "--allow-update-branch",
        ],
    )  # fmt: skip
