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
    
    def test_multiple_numbers(self):
        calculator = StringCalculator()
        assert calculator.add("1, 2, 3, 4, 5") == 15
        assert calculator.add("10, 20, 30, 40, 50") == 150
        assert calculator.add("1, 2, 3, 4, 5, 6, 7, 8, 9, 10") == 55
    
    def test_new_line_separator(self):
        calculator = StringCalculator()
        assert calculator.add("1\n2,3") == 6
        assert calculator.add("10\n20,30\n40,50") == 150
        assert calculator.add("1,2\n3,4\n5,6\n7,8\n9,10") == 55
    
    def test_custom_delimiter(self):
        calculator = StringCalculator()
        assert calculator.add("//;\n1;2") == 3
        assert calculator.add("//|\n1|2|3") == 6
        assert calculator.add("//;\n1;2;3;4;5") == 15
        assert calculator.add("//;\n10;20;30;40;50") == 150
        assert calculator.add("//|\n1|2|3|4|5") == 15
    
    def test_negative_numbers_not_allowed(self):
        calculator = StringCalculator()
        
        with pytest.raises(ValueError, match="negative numbers not allowed: -1"):
            calculator.add("1,-1,2")
        
        with pytest.raises(ValueError, match="negative numbers not allowed: -1, -3"):
            calculator.add("1,-1,2,-3")
        
        with pytest.raises(ValueError, match="negative numbers not allowed: -10, -20"):
            calculator.add("-10, -20, 1, 40")

    def test_negative_with_custom_delimiter(self):
        calculator = StringCalculator()
        
        with pytest.raises(ValueError, match="negative numbers not allowed: -2"):
            calculator.add("//;\n1;-2;3")
        
        with pytest.raises(ValueError, match="negative numbers not allowed: -2"):
            calculator.add("//;\n1;-2;3")
        
        with pytest.raises(ValueError, match="negative numbers not allowed: -1"):
            calculator.add("//|\n6|10|-1")