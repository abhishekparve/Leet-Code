class Solution:
    def postfixToPrefix(self, post_exp):
        i = 0
        n = len(post_exp)
        stack = []
        while i < n:
            if post_exp[i].isalnum():
                # push the operand
                stack.append(post_exp[i])
            else:
                # Pop lat two operands
                t1 = stack.pop()
                t2 = stack.pop()
                # operator + operand + operand
                val = post_exp[i] + t2 + t1
                stack.append(val)
            i += 1
        return stack[-1]


answer = Solution()
post_exp = "ABC/-AK/L-*"
print(answer.postfixToPrefix(post_exp))
