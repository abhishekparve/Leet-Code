class Solution:
    def letterCombinations(self, digits):
        results = []
        digitsToChar = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def backtrack(i, currStr):
            if len(currStr) == len(digits):
                results.append(currStr)
                return
            value = digits[i]
            new = digitsToChar[digits[i]]
            for c in digitsToChar[digits[i]]:
                backtrack(i + 1, currStr + c)
        if digits:
            backtrack(0, "")
        return results

answer = Solution()
result = answer.letterCombinations("23")
print(result)


            