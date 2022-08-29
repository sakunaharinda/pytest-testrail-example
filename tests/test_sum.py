import pytest
from pytest_testrail.plugin import pytestrail
from lib.utils import case
import pytest


@case("C63")
def test_sum_two_numbers():
    assert 1 + 1 == 2


@case("C62")
def test_sum_two_decimals():
    assert 0.8 + 0.3 == 1.2


@case("C65", "C66")
@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6)])
def test_sum_multiple_numbers(test_input, expected):
    assert eval(test_input) == expected


