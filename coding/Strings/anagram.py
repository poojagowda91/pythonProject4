# def isAnagram(str1, str2):
#     str1 = str1.replace(" ", "").lower()
#     str2 = str2.replace(" ", "").lower()
#
#     return sorted(str1) == sorted(str2)
#
#
# str1 = "Mother In Law"
# str2 = "Hitler Woman"
# isAnagram(str1, str2)
#
# if isAnagram(str1, str2):
#     print(f'"{str1}" and "{str2}" are anagrams.')
# else:
#     print(f'"{str1}" and "{str2}" are not anagrams.')


def group_anagrams(strs):
    anagrams = {}

    for word in strs:
        # Sort the characters of the word and use it as a key
        sorted_word = ''.join(sorted(word))

        # Check if the key is already in the hash table
        if sorted_word in anagrams:
            # If yes, append the word to the existing list
            anagrams[sorted_word].append(word)
        else:
            # If no, create a new list with the current word
            anagrams[sorted_word] = [word]

    # Convert the values of the hash table to a list to get the final result
    result = list(anagrams.values())

    return result


# Example usage:
strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
strs2 = [""]
strs3 = ["a"]

print(group_anagrams(strs1))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

print(group_anagrams(strs2))
# Output: [['']]

print(group_anagrams(strs3))
# Output: [['a']]
