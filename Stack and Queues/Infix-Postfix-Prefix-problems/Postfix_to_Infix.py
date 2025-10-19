class Solution:
    # Iterate the String in reverse
    # If you find an operand add it to the stack
    # if you encounter an operator then pop the two elemenst from top t1 and t2
    # and club them together with "(" + 2nd popped (t2) + operator + first popped (t1) + ")"
    # and again add it back to the stack
    # at the end there will be only one single element in the stack so return the top element
    def prefixToInfix(self, s):
        stack = []
        i = 0
        n = len(s)
        while i < n:
            if s[i].isalnum():
                stack.append(s[i])
            else:
                t1 = stack.pop()
                t2 = stack.pop()
                val = "(" + t2 + s[i] + t1 + ")"
                stack.append(val)
            i += 1
        return print(stack[-1])


answer = Solution()
s = "ab*c+"
answer.prefixToInfix(s)
