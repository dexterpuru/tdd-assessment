import pytest
from string_calculator import StringCalculator

class TestStringCalculator:
    def test_empty_string_returns_zero(self):
        calculator = StringCalculator()
        result = calculator.add("")
        assert result == 0