import pytest
from src.main.train.utils import get_title
def get_parameters():
    return ["Allen, Miss. Elisabeth Walton","Miss"]

@pytest.mark.parametrize("name, expected", get_parameters())
def test_get_title(name : str , expected : str):
    assert get_title(name) == expected