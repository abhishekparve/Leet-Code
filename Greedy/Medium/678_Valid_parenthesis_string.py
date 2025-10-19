class Solution:
    # Here in the questions for "*" we have three options
    # this gives us an intution to try recursion by checking all
    # possible combination for "*"
    # Three decision, and it is a recursive approach
    # Therefore, TC = 3 ^ n
    # SC = O(n) ==> n is the length of s
    # NOTE the levels(height) of the tree is also equal to n
    def validParenthesisRecursion(self, s):
        def solve(s, index, count):
            if count < 0:
                return False
            if index == len(s):
                return count == 0

            if s[index] == "(":
                return solve(s, index + 1, count + 1)
            elif s[index] == ")":
                return solve(s, index + 1, count - 1)
            else:
                return (
                    solve(s, index + 1, count + 1)
                    or solve(s, index + 1, count - 1)
                    or solve(s, index + 1, count)
                )

        return solve(s, 0, 0)

    # TC = O(n)
    # SC = O(n)
    # Why indices?
    # Because order matters.
    # You can only match a '*' to an unmatched '(' if it comes after that '(' in the string
    # — this ensures proper nesting.
    def validParenthesisStack(self, s):
        # Using Stack
        # to store indices of "(" and "*"
        open_stack = []
        astericks_stack = []
        for i in range(len(s)):
            if s[i] == "(":
                open_stack.append(i)
            elif s[i] == "*":
                astericks_stack.append(i)
            else:
                if open_stack and s[i] == ")":
                    open_stack.pop()
                elif astericks_stack and s[i] == ")":
                    astericks_stack.pop()
                else:
                    # open_stack is empty case
                    return False

        # Second-pass is needed to balance out the remaining elements astericks stack
        # with the remaining elements in the open_stack
        while open_stack and astericks_stack:
            # If top element of open_stack is greater than the top element
            # of astericks_stack, it means that the top element of astericks_stack
            # must have came earlier than the top element of the open_stack. So it will never match
            if open_stack[-1] > astericks_stack[-1]:
                return False
            # we are popping beacuse the astericks_stack[-1] > open_stack[-1]
            # which means that the top element of the astericks_stack have
            # have come after the top element of open_stack and we can use both of them
            # to balance out
            open_stack.pop()
            astericks_stack.pop()

        # if len(stack) == 0, it means that all the parenthesis are balanced out
        # if open_stack:
        #     return False
        # else:
        #     return True
        # OR
        return len(open_stack) == 0

    # Two Pass Greedy approach
    # TC = O(2n)
    # SC = O(1)
    def validParanthesisGreedy2Pass(self, s):
        # two variables
        open_count = 0
        close_count = 0

        # Left to Right iteration
        # We assume * as "(" and update the open_count by 1
        # this ensure that there are never too many closing parentheses.
        # If open_count becomes < 0. it means that there are too many
        # closing parenthesis  than "(" onces even after assuming
        # "*" as "(" parenthesis. So we return False
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "*":
                open_count += 1
            else:
                # decrementing open_count when we encounter ")" parenthsis
                open_count -= 1
                if open_count < 0:
                    return False

        # Right to Left iteration
        # We assume * as ")" and update the close_count by 1
        # this ensure that there are never too many opening parentheses.
        # If close_count becomes < 0. it means that there are too many
        # opening parenthesis  than ")" onces even after assuming
        # "*" as ")" parenthesis. So we return False
        for j in range(len(s) - 1, -1, -1):
            if s[j] == ")" or s[j] == "*":
                close_count += 1
            else:
                # decrementing close_count when we encounter "(" parenthsis
                close_count -= 1
                if close_count < 0:
                    return False

        return True

    # Range based Greedy approach
    # No so intutive
    # TC = O(n)
    # SC = O(1)
    def validParenthesisRangeBasedGreedy(self, s):
        min_count = 0
        max_count = 0
        for char in s:
            if char == "(":
                min_count += 1
                max_count += 1
            elif char == ")":
                min_count -= 1
                max_count -= 1
            else:
                min_count -= 1
                max_count += 1

            # if min_count < 0, we reset it to zero
            if min_count < 0:
                min_count = 0
            # If there is nothing on the positive side towards the max_count
            # when we are talking about the range, it is impossible to recover
            # [min_count, max_count]
            # if min_count becomes -1 we can reset it to zero
            # but when max_count becomes -1 there is no range and it is not possible
            # to balance the parenthesis
            if max_count < 0:
                return False
        # return true only when min_count becomes zero
        return min_count == 0


answer = Solution()
# s = "(*)("
s = "*(())(*"
print(answer.validParenthesisRecursion(s))
print(answer.validParenthesisStack(s))
print(answer.validParanthesisGreedy2Pass(s))
print(answer.validParenthesisRangeBasedGreedy(s))
