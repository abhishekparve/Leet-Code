# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:

# Input: nums = [0]
# Output: [[],[0]]

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.


# TC = n * O(2**n)
# SC = O(n)
# Approach 1 : Brute force backtracking
class Solution:
    def subsets(self, nums):
        result = []
        subset = []

        def generateSubsets(index, subsets):
            if index == len(nums):
                result.append(subset.copy())
                return
            # Decision 1 : Inculde 1 or value
            subset.append(nums[index])
            generateSubsets(index + 1, subset)

            # Decision 2: Do not include any value
            subset.pop()
            generateSubsets(index + 1, subset)

        generateSubsets(0, subset)
        return result


# Appraoch 2 : Bit Manipulation
class Solution2:
    def subsetsBitwise(self, nums):
        n = len(nums)
        result = []
        for number in range(1 << n):
            subset = []
            for j in range(len(nums)):
                if (number & (1 << j)) != 0:
                    subset.append(nums[j])
            result.append(subset)
        return result


answer = Solution()
answer2 = Solution2()
nums = [1, 2, 3]
# print(answer.subsets(nums))
print(answer2.subsetsBitwise(nums))
