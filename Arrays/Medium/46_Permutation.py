# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

# Example 3:
# Input: nums = [1]
# Output: [[1]]

# The time complexity of this solution is O(n!) because there are n! possible permutations of the input list.
# This is because for each element in the list, we have n-1 choices for the next element,
#  then n-2 choices for the next element, and so on, resulting in n * (n-1) * (n-2) * ... * 1 = n! possible permutations.

# The space complexity of this solution is also O(n!) because we need to store all n! possible permutations in the results list.

class Solution:
    def permute(self, nums):
        results = []

        if len(nums) == 1:
            # Instead of nums.copy(), we can add nums[:]
            print("If nums length is 1:", [nums[:]])
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            results.extend(perms)
            nums.append(n)
        return results
    
answer = Solution()
answer.permute([1, 2, 3])
