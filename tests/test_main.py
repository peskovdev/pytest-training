from app.main import Calculator

import pytest


@pytest.mark.parametrize(
    "x, y, res",
    [
        (-1, 1, 0),
        (5, -1, 4),
    ]
 )
def test_sum(x, y, res):
    assert Calculator().sum(x, y) == res


@pytest.mark.parametrize(
    "x, y, res",
    [
        (1, 2, 0.5),
        (5, -1, -5),
    ]
 )
def test_divide(x, y, res):
    assert Calculator().divide(x, y) == res
