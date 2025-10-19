class Solution:
    def infixToPostfix(self, s):
        n = len(s)
        answer = ""
        stack = []
        i = 0
        while i < len(s):
            if s[i].isalnum():
                answer += s[i]
            elif s[i] == "(":
                stack.append(s[i])
            elif s[i] == ")":
                while len(stack) != 0 and stack[-1] != "(":
                    answer += stack.pop()
                stack.pop()
            else:
                if len(stack) != 0 and self.priority(s[i]) <= self.priority(stack[-1]):
                    answer += stack.pop()
                else:
                    stack.append(s[i])
            i += 1
        while not stack:
            answer += stack.pop()
        return answer

    def priority(self, ch):
        if ch == "^":
            return 3
        elif ch == "*" or ch == "/":
            return 2
        elif ch == "+" or ch == "-":
            return 1
        else:
            return -1


result = Solution()
s = "a+b*(c^d-e)^(f+g*h)-i"
print(result.infixToPostfix(s))
