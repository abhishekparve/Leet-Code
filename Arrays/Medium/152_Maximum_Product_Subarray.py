# Given an integer array nums, find a subarray that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# Example 1:
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Example 2:
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

# The time complexity of this solution is O(n), where n is the length of the input array nums.
# This is because we iterate through the array once, performing a constant number of operations for each element.

# The space complexity is O(1) because we only use a constant amount of extra space to store the current maximum,
# current minimum, and maximum sum.

class Solution:
    def maxProductSubarray(self, nums):
        result = max(nums)
        currMax, currMin = 1, 1
        for n in nums:
            tempMax = n * currMax
            tempMin = n * currMin
            currMax = max(n, tempMax, tempMin)
            currMin = min(n, tempMin, tempMax)
            result = max(result, currMax)
        return print(result)
    
answer = Solution()
answer.maxProductSubarray([2,3,-2,4])
