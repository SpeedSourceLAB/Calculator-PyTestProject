
"""Use conftest.py while running this test"""

def test_add():
    a=2
    b=3
    assert a + b == 6, "Expected: {}, Result: {}".format(a+b,6)

def test_add(numbers):
    assert numbers[0] + numbers[1] == 5, \
        "Expected: {}, Result: {}".format(numbers[0]+numbers[1],5)

def testsubtract(numbers):
    assert numbers[0] - numbers[1] == 3, \
        "Expected: {}, Result: {}".format(numbers[0] - numbers[1], 3)

def testmultiply(numbers):
    assert numbers[0] * numbers[1] == 18, \
        "Expected: {}, Result: {}".format(numbers[0] * numbers[1], 18)

def test_divide(numbers):
    assert (numbers[0] / numbers[1]) == 3, \
        "Expected: {}, Result: {}".format(numbers[0] / numbers[1], 3)



