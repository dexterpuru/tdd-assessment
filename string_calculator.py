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
        
        normalized = numbers.replace('\n', ',')
        return self._add_numbers(normalized.split(','))
    
    def _add_numbers(self, number_strings: list[str]) -> int:
        """
        Convert list of numbers to integers and return their sum.
        """
        return sum(int(num.strip()) for num in number_strings)