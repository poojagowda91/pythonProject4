class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False

        n, r, sum = 0, 0, 0
        temp = x

        while x > 0:
            r = x % 10
            sum = (sum * 10) + r
            x = x // 10

        return temp == sum


# Create an instance of the class
solution_instance = Solution()

# Call the method on the instance
result = solution_instance.isPalindrome(-121)

# Print the result
print(result)
