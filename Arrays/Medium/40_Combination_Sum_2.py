# Given a collection of candidate numbers (candidates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

# Example 1:

# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [[1,2,2],[5]]

# The time complexity of this solution is O(2^n), where n is the length of the candidates list.
# This is because for each candidate, we have two choices - either include it in the current combination or skip it.
# Since we have n candidates, the total number of combinations can be 2^n.

# The space complexity is O(target), as the maximum depth of the recursion stack is equal to the target value.
# Additionally, the result list will store all the valid combinations,
# which can also have a space complexity of O(target) in the worst case.

class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        result = []

        def backTrack(curr, pos, target):
            if target == 0:
                result.append(curr.copy())
            if target <= 0:
                return
            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                curr. append(candidates[i])
                targetMinusCan = target - candidates[i]
                print("target - candidates[i]:", targetMinusCan)
                print("value of i:", i)
                print("Curr:", curr)
                print("Prev:", prev)
                backTrack(curr, i + 1, target - candidates[i])
                curr.pop()
                prev = candidates[i]
        backTrack([], 0, target)
        return print(result)

answer = Solution()
answer.combinationSum([2,5,2,1,2], 5)
                