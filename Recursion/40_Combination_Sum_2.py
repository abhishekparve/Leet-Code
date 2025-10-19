class Solution:
    def combinationSum2(self, candidates, target):
        result = []
        comb = []
        candidates.sort()

        def getCombinations(index, comb, total):
            if total == target:
                result.append(comb.copy())
                return
            if index >= len(candidates) or total > target:
                return
            comb.append(candidates[index])
            getCombinations(index + 1, comb, total + candidates[index])
            comb.pop()
            while (
                index + 1 < len(candidates)
                and candidates[index] == candidates[index + 1]
            ):
                index += 1
            getCombinations(index + 1, comb, total)

        getCombinations(0, comb, 0)
        return result

    # Method 2
    def combiationSum2Method2(self, candidates, target):
        candidates.sort()
        result = []
        comb = []

        def backtrack(index, comb, target):
            if target == 0:
                result.append(comb.copy())
            if target <= 0:
                return

            prev = -1
            for i in range(index, len(candidates)):
                if candidates[i] == prev:
                    continue
                comb.append(candidates[i])
                backtrack(i + 1, comb, target - candidates[i])
                comb.pop()
                prev = candidates[i]

        backtrack(0, comb, target)
        return result


answer = Solution()
# candidates = [10, 1, 2, 7, 6, 1, 5]
# target = 8
candidates = [2, 5, 2, 1, 2]
target = 5

# print(answer.combinationSum2(candidates, target))
print(answer.combiationSum2Method2(candidates, target))
