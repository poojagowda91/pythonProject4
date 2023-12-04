class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        original_words = s.split()
        last_word = original_words[-1]
        value = len(last_word)
        return value


soultioninstance = Solution()
result = soultioninstance.lengthOfLastWord("Hello World")
print(result)

#O(n) - time and space complexity