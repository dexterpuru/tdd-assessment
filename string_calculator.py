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
        
        
        delimiter_pattern, number_string = self._parse_input(numbers)
        number_list = self._split_by_delimiters(number_string, delimiter_pattern)
        
        integer_list = [int(num.strip()) for num in number_list if num.strip()]
        negative_nums = [num for num in integer_list if num < 0]
        
        if negative_nums:
            negative_str = ', '.join(map(str, negative_nums))
            raise ValueError(f"negative numbers not allowed: {negative_str}")
        
        return sum(integer_list)
    
    def _parse_input(self, numbers: str) -> tuple[str, str]:
        """
        Parse input string to extract custom delimiter pattern and number string.
        """
        if numbers.startswith('//'):
            lines = numbers.split('\n', 1)
            custom_delimiter = lines[0][2:] # Remove '//'
            return custom_delimiter, lines[1]
        return ',|\n', numbers # Default delimiters
    
    def _split_by_delimiters(self, text: str, delimiter_pattern: str) -> list[str]:
        """
        Split text into list of strings using the specified delimiter pattern.
        """
        escaped_pattern = re.escape(delimiter_pattern).replace('\\|', '|')
        return re.split(f'[{escaped_pattern}]', text)
