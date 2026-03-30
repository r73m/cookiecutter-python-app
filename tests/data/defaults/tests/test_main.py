from my_python_app.core import get_message


def test_get_message():
    assert get_message() == "Yo!"
