import pytest
from string_calculator import StringCalculator

class TestStringCalculator:
    def test_empty_string_returns_zero(self):
        calculator = StringCalculator()
        result = calculator.add("")
        assert result == 0
    
    def test_single_number_returns_itself(self):
        calculator = StringCalculator()
        assert calculator.add("1") == 1
        assert calculator.add("5") == 5
    
    def test_two_numbers_comma_separated(self):
        calculator = StringCalculator()
        assert calculator.add("10, 5") == 15
        assert calculator.add("10, 20") == 30