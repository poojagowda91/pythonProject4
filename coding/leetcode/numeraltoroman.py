class Solution:
    def intToRoman(self, num: int) -> str:
        roman_numerals = [
            ("M", 1000),
            ("CM", 900),
            ("D", 500),
            ("CD", 400),
            ("C", 100),
            ("XC", 90),
            ("L", 50),
            ("XL", 40),
            ("X", 10),
            ("IX", 9),
            ("V", 5),
            ("IV", 4),
            ("I", 1)
        ]

        result = ""

        for symbol, value in roman_numerals:
            while num >= value:
                result += symbol
                num -= value

        return result

# Example usage:
solution_instance = Solution()
num1 = 3
num2 = 58
num3 = 1994

print(solution_instance.intToRoman(num1))  # Output: "III"
print(solution_instance.intToRoman(num2))  # Output: "LVIII"
print(solution_instance.intToRoman(num3))  # Output: "MCMXCIV"

#The time complexity of the intToRoman method is O(13 * log(num)),
# where 13 is the number of elements in the roman_numerals list.
# The reason for the logarithmic factor is because,
# in the worst case,
# the loop will iterate for each symbol in the roman_numerals list, and in each iteration,
# the number num is reduced by the value of the current symbol.
# The number of iterations is determined by how many times the value of the current symbol can be subtracted from num.
# The maximum number of iterations for each symbol is log(num).