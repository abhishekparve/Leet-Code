# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Example 2:
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.

# The time complexity of this solution is O(n),
# where n is the length of the input list nums. 
# This is because we iterate through the list once, performing constant time operations for each element.

# The space complexity of this solution is O(1),
# as we only use a constant amount of extra space to store the maximum subarray sum and the current sum.

class Solution:
    def maxSubarray(self, nums):
        maxSub = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return print(maxSub)


answer = Solution()
answer.maxSubarray([-2,1,-3,4,-1,2,1,-5,4])