def longest_common_prefix(strs):
    # Check if the input array is empty
    if not strs:
        return ""

    # Find the minimum length string in the array
    min_length_str = min(strs, key=len)

    # Iterate through characters of the minimum length string
    for i, char in enumerate(min_length_str):
        # Check if the character is the same in all strings
        if all(s[i] == char for s in strs):
            continue
        else:
            # If not, return the prefix up to the current character
            return min_length_str[:i]

    # If all characters matched, return the minimum length string
    return min_length_str


# Example usage:
example1 = ["flower", "flow", "flight"]

result1 = longest_common_prefix(example1)

print("Example 1:", result1)


#n summary, the time complexity is O(k * n), and the space complexity is O(k), where k is the average length of strings and n is the number of strings in the array.