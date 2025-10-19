# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Method 1 : Brute Force --> Time Complexity : O(n^2) | Space Complexity : O(1)

class Solution1:
    def two_sum(self, nums, target : int):
        for i in range(len(nums)): # O(n)
            for j in range(i+1, len(nums)): # O(n)
                if nums[i] + nums[j] == target:
                    return print([i,j])
                
answer = Solution1()
nums = [3,2,4]
answer.two_sum(nums, 6) 

# Method 2 :  Time Complexity : O(n) | Space Complexity : O(1)

class Solution2:
    def two_sum(self, nums, target:int):
        for i in range(len(nums)):
            diff = target - nums[i]
            hash_map = {}
            if nums[i] in hash_map:
                return [i, hash_map[nums[i]]]
            else:
                hash_map[diff] = i

answer = Solution2()
nums = [3,3,4,2]
answer.two_sum(nums, 6)


