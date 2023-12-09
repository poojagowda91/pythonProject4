class Solution:
    def convertToTitle(self, n: int) -> str:
        return self.convertToTitle((n - 1) // 26) + \
               chr(ord('A') + (n - 1) % 26) if n else ''

    def convertToNumber(self, title: str) -> int:
        result = 0
        for char in title:
            result = result * 26 + (ord(char) - ord('A') + 1)
        return result


sol = Solution()

# Example: Convert "A" to its corresponding integer value
result = sol.convertToNumber("A")
result2 = sol.convertToTitle(1)
print(result)
print(result2)
