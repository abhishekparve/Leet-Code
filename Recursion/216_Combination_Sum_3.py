# https://leetcode.com/problems/combination-sum-iii/description/


class Solution:
    def combinationSum3(self, k, n):
        result = []
        comb = []

        def backtrack(index, comb, total):
            if total == n and len(comb) == k:
                result.append(comb.copy())
                return
            if len(comb) > k or total > n or index > 9:
                return
            comb.append(index)
            backtrack(index + 1, comb, total + index)
            comb.pop()
            backtrack(index + 1, comb, total)

        backtrack(1, comb, 0)
        return result


answer = Solution()
n = 9
k = 3
print(answer.combinationSum3(k, n))
