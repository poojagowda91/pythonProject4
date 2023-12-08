class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = haystack.find(needle)
        if index != -1:
            print(f"The result is {index}")
        else:
            return -1

        return index


sol = Solution()
sol.strStr("sadbutsad", "sad")
