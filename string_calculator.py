import re

class StringCalculator:
    """
        A calculator that sums numbers from delimited strings.
        
        Supports:
        - Empty strings (returns 0)
        - Single numbers
        - Comma-separated numbers
        - Newline-separated numbers  
        - Custom delimiters in format: //[delimiter]\n[numbers]
        - Validation against negative numbers
    """
    
    DEFAULT_DELIMITERS = ',|\n'
    CUSTOM_DELIMITER_PREFIX = '//'
    
    def add(self, numbers: str) -> int:
        """
        Calculate the sum of numbers in a delimited string.
        
        Args:
            numbers: String containing delimited numbers
            
        Returns:
            Sum of all valid numbers
            
        Raises:
            ValueError: If any negative numbers are found
        """
        if not numbers:
            return 0

        delimiter_pattern, number_string = self._parse_input(numbers)
        number_list = self._split_by_delimiters(number_string, delimiter_pattern)
        integer_list = self._convert_to_integers(number_list)
        self._validate_no_negatives(integer_list)
        return sum(integer_list)
    
    def _convert_to_integers(self, number_list: list[str]) -> list[int]:
        """
        Convert list of string numbers to integers, filtering out empty strings.
        """
        return [int(num.strip()) for num in number_list if num.strip()]

    def _validate_no_negatives(self, integer_list: list[int]) -> None:
        """
        Raise ValueError if any negative numbers are found in the list.
        """
        negative_nums = [num for num in integer_list if num < 0]
        
        if negative_nums:
            negative_str = ', '.join(map(str, negative_nums))
            raise ValueError(f"negative numbers not allowed: {negative_str}")
    
    def _parse_input(self, numbers: str) -> tuple[str, str]:
        """
        Parse input string to extract custom delimiter pattern and number string.
        """
        if numbers.startswith(self.CUSTOM_DELIMITER_PREFIX):
            lines = numbers.split('\n', 1)
            custom_delimiter = lines[0][len(self.CUSTOM_DELIMITER_PREFIX):] # Remove '//'
            return custom_delimiter, lines[1] if len(lines) > 1 else ''
        return self.DEFAULT_DELIMITERS, numbers # Default delimiters
    
    def _split_by_delimiters(self, text: str, delimiter_pattern: str) -> list[str]:
        """
        Split text into list of strings using the specified delimiter pattern.
        """
        if '|' in delimiter_pattern and delimiter_pattern != self.DEFAULT_DELIMITERS:
            # Handle custom delimiters - escape for regex
            escaped = re.escape(delimiter_pattern)
            return re.split(f'[{escaped}]', text)
        else:
            # Use character class for multiple delimiters
            return re.split(f'[{delimiter_pattern}]', text)
