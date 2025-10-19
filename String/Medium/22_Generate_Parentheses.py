# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:
# Input: n = 1
# Output: ["()"]
 
# Constraints:
# 1 <= n <= 8


# Time Complexity:

'''The function generateParenthesis uses a recursive approach to generate all valid combinations of parentheses.
At each recursive call, there are two branches: one for adding an open parenthesis and another for adding a close parenthesis.
The depth of recursion is at most 2n, as at each step, either an open or a close parenthesis is added until both counts of open
and close parentheses reach n.
At each level of recursion, constant-time operations are performed such as appending or popping from the stack and comparing counts.
Therefore, the time complexity is O(2^2n), which simplifies to O(4^n) asymptotically.

Space Complexity:

The space complexity is primarily determined by the recursion stack and the stack list used to keep track of the current combination of parentheses.
In the worst case, the recursion depth can be 2n, corresponding to the maximum number of parentheses pairs.
Additionally, the size of the stack list can be at most 2n as well because at each step, an open or close parenthesis
is appended and later popped.
Therefore, the space complexity is O(n) for the recursion stack and O(n) for the stack list, 
leading to a total space complexity of O(n).'''

class Solution:
    def generateParenthesis(self, n):
        stack = []
        result = []
        def generate(open, close):
            if open == close == n:
                result.append("".join(stack))
                return
            if open < n:
                stack.append("(")
                generate(open + 1, close)
                stack.pop()
            if close < open:
                stack.append(")")
                generate(open, close + 1)
                stack.pop()
        generate(0,0)
        return print(result)

answer = Solution()
answer.generateParenthesis(3)