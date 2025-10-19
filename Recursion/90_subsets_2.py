# Given an integer array nums of unique elements, return all possible
# subsets (the power set).

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

# TC = n*log(n) + n * O(2**n) ~ n*log(n) is insignificant compared to n * O(2**n)
# SC = O(n)


class Solution:
    def subset2(self, nums):
        result = []
        subset = []
        # Sorting the list to ensure that the duplicate values are next to each other
        nums.sort()

        def generateSubset(index, subset):
            if index == len(nums):
                result.append(subset.copy())
                return

            # Decision 1: Adding a value to the subset and futher going down along that path
            subset.append(nums[index])
            generateSubset(index + 1, subset)

            # Decision 2: Pop out the value that we had added in decision 1
            subset.pop()

            # Incrementing the index if we identify that the value at curr index in nums
            # is equal to its next index. We keep on incrementing the index until the value at curr index
            # and its next index are not equal
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1

            # Pass subset as an empty value and further going down along that path
            generateSubset(index + 1, subset)

        generateSubset(0, subset)
        return result


answer = Solution()
nums = [1, 2, 2]
print(answer.subset2(nums))
