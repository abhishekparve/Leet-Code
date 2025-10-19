import sys

sys.setrecursionlimit(10**6)


class Solution:
    # METHOD 1 : Brute
    # TC = O(n) and SC = O(n)
    def reverse(self, stack):
        if not stack:
            return

        # Step 1: Remove the top element
        top = stack.pop()

        # Step 2: Reverse the remaining stack
        self.reverse(stack)

        # Step 3: Push the removed element to the bottom of the stack using a temporary stack
        temp_stack = []

        # Move all elements from the original stack to the temporary stack
        while stack:
            temp_stack.append(stack.pop())

        # Push the original top element to the bottom of the original stack
        stack.append(top)

        # Move all elements back from the temporary stack to the original stack
        while temp_stack:
            stack.append(temp_stack.pop())

    def reverseOptimal(self, stack):
        if not stack:
            return
        top = stack.pop()
        self.reverseOptimal(stack)
        self.insert_at_bottom(stack, top)

    def insert_at_bottom(self, stack, elem):
        if not stack:
            stack.append(elem)
            return
        top = stack.pop()
        self.insert_at_bottom(stack, elem)
        stack.append(top)


stack = [3, 2, 1, 7, 6]
answer = Solution()
# answer.reverse(stack)
# print(stack)
answer.reverseOptimal(stack)
print(stack)
