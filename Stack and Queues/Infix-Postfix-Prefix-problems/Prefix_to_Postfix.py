class Solution:
    # Since it is prefix expression we have to iterate it in reverse
    def prefixToPostfix(self, pre_exp):
        i = len(pre_exp) - 1
        stack = []
        while i >= 0:
            if pre_exp[i].isalnum():
                stack.append(pre_exp[i])
            else:
                t1 = stack.pop()
                t2 = stack.pop()
                val = t1 + t2 + pre_exp[i]
                stack.append(val)
            i -= 1
        return stack[-1]


answer = Solution()
pre_exp = "*-A/BC-/AKL"
print(answer.prefixToPostfix(pre_exp))
