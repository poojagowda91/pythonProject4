def roman_to_int(s):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0
    prev_value = 0

    for symbol in s:
        value = roman_dict[symbol]

        if value > prev_value:
            result += value - 2 * prev_value  # Subtract twice the previous value
        else:
            result += value

        prev_value = value

    return result


# Example usage:
roman_numeral = "MCMXCIV"
integer_value = roman_to_int(roman_numeral)
print(integer_value)  # Output: 27

# Check if the current value is greater than the previous value.
# If it is, this indicates a subtractive notation (e.g., IV for 4 or IX for 9).
# In this case, you subtract twice the previous value from the result and add the current value.
# This is done to account for cases where the smaller numeral appears before the larger one.
# For example, IV represents 4 (5 - 1) and IX represents 9 (10 - 1).

# If the current value is not greater than the previous value, simply add the current value to the result.
