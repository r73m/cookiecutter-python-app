import json
import subprocess


def run(command):
    process = subprocess.run(
        args=command.split(),
        capture_output=True,
        check=True,
        text=True,
    )

    return process.stdout.strip()


commit_hash = run("git rev-parse --short HEAD")

path = "cookiecutter.json"
with open(path) as file:
    cookiecutter = json.load(file)

cookiecutter["_template_version"] = commit_hash

with open(path, "w") as file:
    json.dump(cookiecutter, file, indent=4)
