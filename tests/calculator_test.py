"""Testing the Calculator"""
# From specifies the namespace
from calculator import Calculator


# this defines a test must say test_
def test_calculator_is_instance():
    """Testing the Calculator"""
    # instantiating the Calculator class
    calculator = Calculator()
    # checking that calculator variable contains an instance of Calculator class
    assert isinstance(calculator, Calculator)


def test_calculator_get_result_method():
    """Testing the Calculator"""
    calculator = Calculator()
    # this checks the calculator get result method
    assert calculator.get_result() == 0


def test_calculator_result_property():
    """Testing the Calculator"""
    calc1 = Calculator()
    calc2 = Calculator()
    #  ^these show multiple calculator classes being instantiated and used independently
    calc1.result = 5
    calc2.result = 6
    assert calc1.result == 5
    assert calc2.result == 6


def test_calculator_add_method():
    """Testing the Calculator"""
    calculator = Calculator()
    # this is show using the calculator object add method
    assert calculator.add(1, 1) == 2


def test_calculator_subtract_method():
    """Testing the Calculator Subtract"""
    calculator = Calculator()
    assert calculator.subtract(1, 1) == 0


def test_calculator_multiply_method():
    """Testing the Calculator Subtract"""
    calculator = Calculator()
    assert calculator.multiply(1, 1) == 1


def test_my_first_test_add():
    """Testing the simplest addition"""
    assert 1 + 1 == 2

def test_my_first_test_add_with_variables():
    """Testing the simplest addition"""
    value_a = 1
    value_b = 2
    value_c = value_a + value_b
    assert value_a + value_b == value_c


def test_calculator_divide_method():
    """Testing the calculator Division"""
    value_a = 8
    value_b = 2
    value_c = value_a / value_b
    calculator = Calculator()
    assert calculator.divide(value_a, value_b) == value_c


def test_my_first_test_subtract_with_variables():
    """Testing the simplest addition"""
    value_a = 4
    value_b = 1
    value_c = value_a - value_b
    calculator = Calculator()
    assert calculator.subtract(value_a, value_b) == value_c


def test_my_first_test_multiply_with_variables():
    """Testing the simplest addition"""
    value_a = 1
    value_b = 6
    value_c = value_a * value_b
    calculator = Calculator()
    assert calculator.multiply(value_a, value_b) == value_c


def test_my_second_test_subtract_with_variable():
    """Testing the simplest subtraction"""
    value_a = 6
    value_b = 2
    value_c = value_a - value_b
    calculator = Calculator()
    assert calculator.subtract(value_a, value_b) == value_c


def test_my_second_test_calculator_divide_method():
    """Testing the calculator Division"""
    value_a = 2
    value_b = 2
    value_c = value_a / value_b
    calculator = Calculator()
    assert calculator.divide(value_a, value_b) == value_c
