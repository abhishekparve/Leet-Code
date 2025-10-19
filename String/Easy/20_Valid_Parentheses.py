# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:

# Input: s = "()[]{}"
# Output: true

# Example 2:

# Input: s = "(]"
# Output: false

# The time complexity of this function is O(n), where n is the length of the input string s.
# This is because we iterate through each character in the string once.

# The space complexity is O(n) as well. In the worst case, if all the characters in the string are opening brackets,
# the stack will contain all of them. Therefore, the space required is proportional to the length of the input string.


class Solution:
    def validParentheses(self, s):
        pairs = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)
            elif len(stack) == 0 or bracket != pairs[stack.pop()]:
                return print("False")
        if len(stack) == 0:
            return print("True")
        else:
            return print("False")


answer = Solution()
answer.validParentheses("(]{}")
