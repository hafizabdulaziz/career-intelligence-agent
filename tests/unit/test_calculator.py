import pytest
from calculator_project.calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_add(calculator):
    assert calculator.add(5, 3) == 8.0
    assert calculator.add(-1, 1) == 0.0
    assert calculator.add(1.5, 2.5) == 4.0

def test_subtract(calculator):
    assert calculator.subtract(10, 4) == 6.0
    assert calculator.subtract(5, 8) == -3.0
    assert calculator.subtract(2.5, 0.5) == 2.0

def test_multiply(calculator):
    assert calculator.multiply(4, 7) == 28.0
    assert calculator.multiply(-2, 3) == -6.0
    assert calculator.multiply(0, 10) == 0.0

def test_divide(calculator):
    assert calculator.divide(10, 2) == 5.0
    assert calculator.divide(7, 2) == 3.5
    assert calculator.divide(-6, 3) == -2.0

def test_divide_by_zero(calculator):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(10, 0)
