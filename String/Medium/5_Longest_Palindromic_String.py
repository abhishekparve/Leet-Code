# Given a string s, return the longest 
# palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters.

# The time complexity of this solution is O(n^2), where n is the length of the input string.
# This is because for each character in the string, we expand around it to check for palindromes,
# which takes O(n) time. Since we do this for each character, the overall time complexity is O(n^2).

# The space complexity of this solution is O(1) because we are not using any additional data structures
# that grow with the input size. We only use a constant amount of space to store the result.

class Solution:
    def longestPalindromicString(self, s):
        def expand(l, r):
            while l >= 0 and r < len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r] 
        result = ""
        for i in range(len(s)):
            sub1 = expand(i,i)
            if len(sub1) > len(result):
                result = sub1
            sub2 = expand(i, i + 1)
            if len(sub2) > len(result):
                result = sub2
        return print(result)

answer = Solution()
answer.longestPalindromicString("babad")
    
