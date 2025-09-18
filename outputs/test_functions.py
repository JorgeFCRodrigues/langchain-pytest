import pytest
from examples.functions import soma, subtrai, divide

def test_soma_happy():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0

def test_soma_fail():
    with pytest.raises(TypeError):
        soma("a", 1)

def test_subtrai_happy():
    assert subtrai(5, 3) == 2
    assert subtrai(0, 5) == -5

def test_subtrai_fail():
    with pytest.raises(TypeError):
        subtrai("a", 2)

def test_divide_happy():
    assert divide(6, 3) == 2
    assert divide(1, 2) == 0.5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
