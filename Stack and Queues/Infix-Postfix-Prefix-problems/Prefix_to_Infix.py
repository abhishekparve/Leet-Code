class Solution:
    # Iterate the String in reverse
    # If you find an operand add it to the stack
    # if you encounter an operator then pop the two elemenst from top t1 and t2
    # and club them together with "(" + t1 + operator + t2 + ")"
    # and again add it back to the stack
    # at the end there will be only one single element in the stack so return the top element

    def prefixToInfix(self, pre_exp):
        i = len(pre_exp) - 1
        stack = []
        while i >= 0:
            if pre_exp[i].isalnum():
                stack.append(pre_exp[i])
            else:
                t1 = stack.pop()
                t2 = stack.pop()
                val = "(" + t1 + pre_exp[i] + t2 + ")"
                stack.append(val)
            i -= 1
        return stack[-1]


answer = Solution()
pre_exp = "*-A/BC-/AKL"
print(answer.prefixToInfix(pre_exp))
