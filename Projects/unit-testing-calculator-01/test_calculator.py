# test_calculator.py
from calculator import add

def test_add_positive_numbers():
    """Tests adding two positive numbers."""
    assert add(2, 3) == 5