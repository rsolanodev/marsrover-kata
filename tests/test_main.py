import pytest

from passporter.main import start


def test_main_start():
    with pytest.raises(NotImplementedError):
        start()
