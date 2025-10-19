# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

# The time complexity of this solution is O(n^2), where n is the length of the input list nums.
# This is because we have a nested loop that iterates through the list twice, resulting in a quadratic time complexity.

# The space complexity of this solution is O(1), as we are not using any additional data structures that grow with the input size.
# We are only using a constant amount of space to store the answer list.

class Solution:
    def threeSum(self, nums):
        nums.sort()
        answer = []
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                break
            if i > 0 and nums[i] == nums[i -1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    triplet = [nums[i], nums[l], nums[r]]
                    answer.append(triplet)
                    while (l < r and nums[l] == triplet[1]):
                        l += 1
                    while (l < r and nums[r] == triplet[2]):
                        r -= 1
        return print(answer)

answer = Solution()
answer.threeSum([-1,0,1,2,-1,-4])