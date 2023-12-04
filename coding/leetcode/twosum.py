from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the indices of numbers
        num_to_index = {}

        # Iterate through the list of numbers along with their indices
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach the target
            complement = target - num

            # Check if the complement is already in the dictionary
            if complement in num_to_index:
                # Return the indices of the two numbers whose sum is the target
                return [num_to_index[complement], i]

            # If the complement is not in the dictionary, store the current number and its index
            num_to_index[num] = i

        # If no solution is found, raise a ValueError
        raise ValueError("No solution found")


# Example usage:
arr = [2, 7, 11, 15]
target = 9
solution = Solution()
result = solution.twoSum(arr, target)
print(result)


#O(n) - where n is the length of the input nums.
# It uses a single pass through the list and constant-time lookups in the hash table.
# The use of the hash table significantly improves the efficiency of the solution compared to a brute-force approach.