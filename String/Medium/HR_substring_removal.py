# Given a string s, that consist on only characters "A" and "B". In one move,
# You have to delete either an "AB" or "BB" substring and concatenate the remaining substrings

# Find the minimum possible lenght of the remaining string after performing any number of moves
# Note : A substring is a contiguous subsequence of a string

# Example:
# Input : s = "BABBA"
# Output : 0

# Explaination:
# 1. Delete the substring "AB" starting at the index
"""BABBA"""  # --> "BBA"
# 2. Delete the substring "BB" starting at index 0.
"""BBA"""  # --> "A"


class Solution:
    def minimum_length(self, s):
        stack = []
        i = 0
        while i < len(s):
            if stack and stack[-1] == "A" and s[i] == "B":
                stack.pop()
            elif stack and stack[-1] == "B" and s[i] == "B":
                stack.pop()
            else:
                stack.append(s[i])
            i += 1
        return len(stack)


answer = Solution()
s = "AABBBAB"
s2 = "BABB"
result = answer.minimum_length(s2)
print(result)
