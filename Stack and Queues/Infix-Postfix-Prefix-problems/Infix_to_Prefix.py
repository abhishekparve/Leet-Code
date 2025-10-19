class Solution:
    # Steps:
    # Reverse the string and replace open brackets with close and vice versa
    # Perform same infix to post fix operation but with some conditional changes
    # if you encounter the "^" operator then keep poping the stack until the prior[s[i]] <= prior[stack[-1]]
    # which means two power operator cannot be in the string. Add the popped elements to the answer string
    # else
    # if you encounter any operator prior < priority[stack[-1]]. Pop the operator and add it to the final answer string
    # else: (if greater or =) then push it to the stack
    # check if stack is not empty then keep poping and add the popped elements to the answer string
    # return the reversed answer string

    def priority(self, ch):
        if ch == "^":
            return 3
        elif ch == "*" or ch == "/":
            return 2
        elif ch == "+" or ch == "-":
            return 1
        else:
            return -1

    def reverse_and_swap_brackets(self, s):
        l = 0
        r = len(s) - 1
        s = [ch for ch in s]
        while l <= r:
            while l <= r:
                if s[l] == "(":
                    s[l] = ")"
                elif s[l] == ")":
                    s[l] = "("

                if s[r] == "(":
                    s[r] = ")"
                elif s[r] == ")":
                    s[r] = "("

                # swap
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return "".join(s)

    def infix_to_prefix(self, s):
        s = self.reverse_and_swap_brackets(s)
        stack = []
        answer = ""
        n = len(s)
        i = 0
        while i < n:
            if s[i].isalnum():
                answer += s[i]
            elif s[i] == "(":
                stack.append(s[i])
            elif s[i] == ")":
                while len(stack) != 0 and stack[-1] != "(":
                    answer += stack.pop()
                stack.pop()
            else:
                if s[i] == "^":
                    while len(stack) != 0 and self.priority(s[i]) <= self.priority(
                        stack[-1]
                    ):
                        answer += stack.pop()
                else:
                    while len(stack) != 0 and self.priority(s[i]) < self.priority(
                        stack[-1]
                    ):
                        answer += stack.pop()
                    stack.append(s[i])
            i += 1

        while len(stack) != 0:
            answer += stack.pop()
        # We can use the same fuction for reverse because the brackets will not be there in tha answer
        answer = self.reverse_and_swap_brackets(answer)
        return print(answer)


answer = Solution()
s = "x+y*z/w+u"
answer.infix_to_prefix(s)
