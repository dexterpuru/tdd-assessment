class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0
        number_list = numbers.split(',')
        return sum(int(num) for num in number_list)