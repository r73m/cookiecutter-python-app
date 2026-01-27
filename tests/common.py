import tomllib
from pathlib import Path

from cookiecutter.main import cookiecutter

_THIS_FILE = Path(__file__)
THIS_DIR = _THIS_FILE.parent

DATA_DIR = THIS_DIR / "data"
TEMPLATE_DIR = THIS_DIR.parent

DEFAULT_SLUG = "my-python-app"


def generate_project(output_dir, **context):
    if context:
        context = {k: v for k, v in context.items() if v is not None}

    cookiecutter(
        template=str(TEMPLATE_DIR),
        no_input=True,
        extra_context=context or None,
        output_dir=output_dir,
    )

    slug = context.get("slug", DEFAULT_SLUG)
    return output_dir / slug


def load_project_meta(project_dir):
    meta_path = project_dir / "pyproject.toml"
    return load_toml(meta_path)


def load_toml(path):
    with open(path, "rb") as file:
        return tomllib.load(file)
