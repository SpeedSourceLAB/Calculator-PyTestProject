from Calculator.Calculator.Calculator import Calculator

"""Use conftest.py while running this test"""

c= Calculator()

def test_add(numbers_csv):
    for set in numbers_csv.index:
        print(set)
        print(numbers_csv['num1'][set], numbers_csv['num2'][set])
        result = c.add(numbers_csv['num1'][set], numbers_csv['num2'][set])
        print(result, numbers_csv['add'][set])
        assert result== numbers_csv['add'][set], "Actual: {}, Expected: {}".format(result,numbers_csv['add'][set])

def test_subtract(numbers_csv):
    for set in numbers_csv.index:
        #print(numbers_csv['num1'][set], numbers_csv['num2'][set])
        result = c.subtract(numbers_csv['num1'][set], numbers_csv['num2'][set])
        assert result== numbers_csv['sub'][set], "Actual: {}, Expected: {}".format(result,numbers_csv['sub'][set])

def test_multiply(numbers_csv):
    for set in numbers_csv.index:
        #print(numbers_csv['num1'][set], numbers_csv['num2'][set])
        result = c.multiply(numbers_csv['num1'][set], numbers_csv['num2'][set])
        assert result== numbers_csv['multi'][set], "Actual: {}, Expected: {}".format(result,numbers_csv['multi'][set])

def test_divide(numbers_csv):
    for set in numbers_csv.index:
        #print(numbers_csv['num1'][set], numbers_csv['num2'][set])
        result = c.divide(numbers_csv['num1'][set], numbers_csv['num2'][set])
        assert result== numbers_csv['div'][set], "Actual: {}, Expected: {}".format(result,numbers_csv['div'][set])


# def teardown_module():
#     print("teardown_module")
#
# def setup_module():
#     print("setup_module")
#
# def setup_function():
#     print("  setup_function")
#
# def teardown_function():
#     print("  teardown_function")
