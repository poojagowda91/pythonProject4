def isValid(s):
    stack = []
    bracket_mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_mapping.values():
            stack.append(char)
        elif char in bracket_mapping.keys():
            if not stack or bracket_mapping[char] != stack.pop():
                return False
        else:
            # Invalid character
            return False

    # The stack should be empty if the string is valid
    return not stack


# Example usage:
print(isValid("()"))  # Output: True
print(isValid("()[]{}"))  # Output: True
print(isValid("(]"))  # Output: False

#Closing Brackets:If the character is a closing bracket (i.e., it is in the keys of bracket_mapping), we check if the stack is not empty and if the corresponding opening bracket matches the last one in the stack. If it doesn't match, the string is invalid, and we return False.
#Invalid Characters:If the character is neither an opening nor a closing bracket, it is an invalid character, and we immediately return False.

#O(n)