from filecmp import dircmp
from pathlib import Path

from cookiecutter.main import cookiecutter

THIS_FILE = Path(__file__)
THIS_DIR = THIS_FILE.parent
DATA_DIR = THIS_DIR / "data"
TEMPLATE = str(THIS_DIR.parent)  # must be `str`


def test_everything(tmp_path):
    out_dir = str(tmp_path)  # `tmp_path` is `pathlib.Path`
    cookiecutter(TEMPLATE, no_input=True, output_dir=out_dir)

    actual_dir = tmp_path / "my-python-app"
    expected_dir = DATA_DIR / "defaults"

    difference = dircmp(actual_dir, expected_dir, ignore=[".git", "uv.lock"])

    assert not difference.left_only, f"Extra files {difference.left_only}"
    assert not difference.right_only, f"Missing files {difference.right_only}"
    assert not difference.diff_files, f"Different files {difference.diff_files}"

    git_dir = actual_dir / ".git"
    assert git_dir.is_dir(), "Not a Git repo"
