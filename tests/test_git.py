import git
from pytest import Subtests

from common import generate_project


# subtests allow to avoid recreating the project
def test_git_repo(tmp_path, subtests: Subtests):
    # WHEN
    project_dir = generate_project(tmp_path)

    # THEN
    repo = git.Repo(project_dir)

    with subtests.test("not dirty"):
        assert not repo.is_dirty()

    with subtests.test("single branch"):
        assert len(repo.branches) == 1

    with subtests.test("single commit"):
        assert len(list(repo.iter_commits())) == 1

    with subtests.test("commit message"):
        # TODO Check in full once defaults are done
        template = "gh:r73m/cookiecutter-python-app"
        assert template in repo.head.commit.message
