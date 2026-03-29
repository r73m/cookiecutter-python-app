from {{ cookiecutter.package }}.core import get_message


def main():
    print(get_message())
