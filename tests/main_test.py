import tomllib
from filecmp import dircmp
from pathlib import Path

from cookiecutter.main import cookiecutter
from pytest import mark

THIS_FILE = Path(__file__)
THIS_DIR = THIS_FILE.parent
DATA_DIR = THIS_DIR / "data"
TEMPLATE = str(THIS_DIR.parent)  # must be `str`
DEFAULT_SLUG = "my-python-app"


def test_everything(tmp_path):
    # given
    expected_dir = DATA_DIR / "defaults"

    # when
    actual_dir = generate_project(tmp_path)

    # then
    difference = dircmp(actual_dir, expected_dir, ignore=[".git", "uv.lock"])
    assert not difference.left_only, f"Extra files {difference.left_only}"
    assert not difference.right_only, f"Missing files {difference.right_only}"
    assert not difference.diff_files, f"Different files {difference.diff_files}"

    git_dir = actual_dir / ".git"
    assert git_dir.is_dir(), "Not a Git repo"


@mark.parametrize(
    "slug,expected",
    [
        (None, DEFAULT_SLUG),
        ("foo", "foo"),
    ],
)
def test_project_dir_name(tmp_path, slug, expected):
    # given
    expected_dir = tmp_path / expected

    # when
    generate_project(tmp_path, slug=slug)

    # then
    assert expected_dir.is_dir()


@mark.parametrize(
    "slug,expected",
    [
        (None, DEFAULT_SLUG),
        ("foo", "foo"),
    ],
)
def test_project_name(tmp_path, slug, expected):
    # when
    project_dir = generate_project(tmp_path, slug=slug)

    # then
    meta = load_project_meta(project_dir)
    project_name = meta["project"]["name"]
    assert project_name == expected


@mark.parametrize(
    "slug,command,expected",
    [
        (None, None, DEFAULT_SLUG),
        ("foo", None, "foo"),
        (None, "bar", "bar"),
        ("foo", "bar", "bar"),
    ],
)
def test_command_name(tmp_path, slug, command, expected):
    # given
    context = {"slug": slug, "command": command}

    # when
    project_dir = generate_project(tmp_path, **context)

    # then
    meta = load_project_meta(project_dir)
    scripts = meta["project"]["scripts"]
    assert len(scripts) == 1

    actual_command = next(iter(scripts))
    assert actual_command == expected


def generate_project(output_dir, **context):
    if context:
        context = {k: v for k, v in context.items() if v is not None}

    cookiecutter(
        template=TEMPLATE,
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
