import pytest

from Calculator.Calculator.Calculator import Calculator
"""Use conftest.py while running this test"""

c= Calculator()

@pytest.mark.xfail
def test_input_value_is_integer(numbers):
    result =c.numbers_is_integer(numbers)
    assert result == True

def test_add(numbers):
    result = c.add(numbers[0], numbers[1])
    assert result == 12, "Expected: {}, Result: {}".format(result, 12)

def testsubtract(numbers):
    result = c.subtract(numbers[0], numbers[1])
    assert result == 6, "Expected: {}, Result: {}".format(result, 6)

def testmultiply(numbers):
    result = c.multiply(numbers[0], numbers[1])
    assert result == 27, "Expected: {}, Result: {}".format(result, 27)

def test_divide(numbers):
    result = c.divide(numbers[0], numbers[1])
    assert result == 6, "Expected: {}, Result: {}".format(result, 3)


def test_divide_by_zero():
    a= 10
    b =0
    result = c.divide(a,b)
    assert result == "Infinity", "Expected: {}, Result: {}".format(result, "Infinity")

