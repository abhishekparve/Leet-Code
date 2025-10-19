# https://leetcode.com/problems/palindrome-partitioning/


# TC = 2^n * n
# SC = O(n)
class Solution:
    def partition(self, s):
        result = []
        part = []

        def backtrack(index):
            if index >= len(s):
                result.append(part.copy())
                return

            for j in range(index, len(s)):
                if self.isPalindrome(s, index, j):
                    part.append(s[index : j + 1])
                    backtrack(j + 1)
                    part.pop()

        backtrack(0)
        return result

    def isPalindrome(self, s, l, r):
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


answer = Solution()
s = "aabb"
print(answer.partition(s))
