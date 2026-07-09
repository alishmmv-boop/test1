import pytest
from main import calculate_average, multiply

def test_calculate_average():
    assert calculate_average([10,20,30]) == 20.0
    assert calculate_average([]) == 0.0
    assert calculate_average([5]) == 5.0  

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5