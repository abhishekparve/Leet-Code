# Given an integer array nums of length n and an integer target,
# find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# Example 2:
# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).


# The time complexity of this solution is O(n^2), where n is the length of the input list nums.
# This is because we have nested loops - the outer loop iterates through each element in nums,
# and the inner loop iterates through the remaining elements to find pairs that sum to the target.
# Since the inner loop is dependent on the size of the input, the time complexity is quadratic.

# The space complexity of this solution is O(1) because we are not using any additional data structures that grow with the input size.
# We only need a few variables to keep track of the minimum difference, the current sum, and the result sum.

class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        min_difference = float('inf')
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while (l < r):
                sum = nums[i] + nums[l] + nums[r]
                if sum == target:
                    return target
                elif sum < target:
                    l += 1
                else:
                    r -= 1
                difference_to_target = abs(sum - target)
                if difference_to_target < min_difference:
                    resultSum = sum
                    min_difference = difference_to_target
        return print(resultSum)

answer = Solution()
answer.threeSumClosest([0, 0, 0], 1)