import pytest

def simpleMath(inputValue):
    return inputValue * 5

def test_simpleMath():
    assert simpleMath(5) == 25
    assert simpleMath(3) == 15

    