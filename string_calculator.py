import re

class StringCalculator:
    def add(self, numbers: str) -> int:
        """
        Calculate sum of comma-separated numbers in a string.
        
        Args:
            numbers: String containing comma-separated numbers
            
        Returns:
            Sum of all numbers
        """
        if not numbers:
            return 0
        
        
        delimiter_pattern, number_string = None, None
        
        
        if numbers.startswith('//'):
            lines = numbers.split('\n', 1)
            delimiter_pattern = lines[0][2:] # Remove '//'
            number_string = lines[1]
        else:
            delimiter_pattern = ',|\n'
            number_string = numbers
        
        escaped_pattern = re.escape(delimiter_pattern).replace('\\|', '|')
        number_list = re.split(f'[{escaped_pattern}]', number_string)
        
        return self._add_numbers(number_list)
    
    def _add_numbers(self, number_strings: list[str]) -> int:
        """
        Convert list of numbers to integers and return their sum.
        """
        return sum(int(num.strip()) for num in number_strings)