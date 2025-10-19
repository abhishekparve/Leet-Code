# https://leetcode.com/problems/combinations/description/


# TC = O(2^n)
# SC = O(n)
class Solution:
    def combinations(self, n, k):
        result = []
        comb = []

        # METHOD I
        def generateCombinations(start, k, comb):
            if k == 0:
                result.append(comb.copy())
                return

            # if index > n:
            #     return

            for index in range(start, n + 1):
                comb.append(index)
                generateCombinations(index + 1, k - 1, comb)
                comb.pop()

        generateCombinations(1, k, comb)
        return result

        # METHOD II
        # def getCombinations(index, k, comb):
        #     if k == 0:
        #         result.append(comb.copy())
        #         return

        #     if index > n:
        #         return

        #     comb.append(index)
        #     getCombinations(index + 1, k - 1,  comb)
        #     comb.pop()
        #     getCombinations(index + 1, k,  comb)


answer = Solution()
n = 4
k = 2
print(answer.combinations(n, k))
