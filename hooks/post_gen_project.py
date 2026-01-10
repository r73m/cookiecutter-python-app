import subprocess
from collections import OrderedDict
from typing import Any


def run(*commands):
    for command in commands:
        if isinstance(command, str):
            command = command.split()
        subprocess.run(command, check=True)


def to_shell(value):
    if isinstance(value, bool):
        return "y" if value else "n"
    value = str(value)
    if " " in value:
        return f"'{value}'"
    return value


params: OrderedDict[str, Any] = {{ cookiecutter }}  # type: ignore  # noqa: F821  # fmt: skip

suffix = " \\\n"
commit_message = f"""\
Initial commit

Generated with an equivalent of the following command:
cookiecutter \\
    --no-input --checkout {params["_template_version"]} \\
    gh:r73m/cookiecutter-python-app \\
{
    suffix.join(
        f"    {key}={to_shell(value)}"
        for key, value in params.items()
        if not key.startswith("_")
    )
}
"""

run(
    "uv lock", "git init", "git add .",
    ["git", "commit", "--message", commit_message],
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
