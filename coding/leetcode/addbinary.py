def addBinary(a, b):
    # Convert binary strings to integers
    a_int = int(a, 2)
    b_int = int(b, 2)

    # Add the integers
    sum_int = a_int + b_int

    # Convert the sum back to a binary string
    result = bin(sum_int)[2:]

    return result

# Example usage
a = "11"
b = "1"
result = addBinary(a, b)
print(result)  # Output: "100"

a = "1010"
b = "1011"
result = addBinary(a, b)
print(result)  # Output: "10101"
