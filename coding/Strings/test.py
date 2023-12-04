from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the least significant digit
        for i in range(len(digits) - 1, -1, -1):
            # Increment the current digit
            digits[i] += 1
            # If the digit becomes 10, set it to 0 and carry 1 to the next digit
            if digits[i] == 10:
                digits[i] = 0
            else:
                # If the digit is less than 10, no need to carry, break the loop
                break

        # If the most significant digit becomes 10, insert a new digit at the beginning
        if digits[0] == 0:
            digits.insert(0, 1)

        return digits


# Examples
sol = Solution()
print(sol.plusOne([1, 2, 3]))  # Output: [1, 2, 4]
print(sol.plusOne([4, 3, 2, 1]))  # Output: [4, 3, 2, 2]
print(sol.plusOne([9]))  # Output: [1, 0]
