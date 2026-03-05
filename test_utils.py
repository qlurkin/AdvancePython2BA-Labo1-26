import pytest
import utils
import math


def test_fact():
    assert utils.fact(5) == 120
    with pytest.raises(ValueError):
        utils.fact(-5)


def test_roots():
    assert utils.roots(1, 0, 1) == tuple()
    assert utils.roots(1, 0, 0) == (0,)
    assert utils.roots(1, 0, -4) == (-2, 2)


def test_integrate():
    assert math.isclose(utils.integrate("2*x", 0, 4), 16.0)
