class MinStack:
    # Optimal approach
    # TC = O(1) and SC= O(n)
    # min value about to be inserted  < min Value in stack
    # 10  < 12
    # val < minValue
    # val - minValue < 0
    # adding val on both sides
    # val + val - minValue < val
    # 2 val - minValue < val
    # newMinValue < val

    def __init__(self):
        self.stack = []
        self.minElem = float("inf")

    def push(self, val):
        if len(self.stack) == 0:
            self.stack.append(val)
            self.minElem = val
        else:
            if val < self.minElem:
                self.stack.append(2 * val - self.minElem)
                self.minElem = val
            else:
                self.stack.append(val)
        return print(self.stack)

    def pop(self):
        if len(self.stack) == 0:
            return print("Stack is empty")
        else:
            val = self.stack.pop()
            if val < self.minElem:
                popped_elem = self.minElem
                self.minElem = 2 * self.minElem - val
                return print(popped_elem)
            return print(val)

    def top(self):
        if len(self.stack) == 0:
            return print("Stack is empty")
        else:
            if self.stack[-1] < self.minElem:
                return print(self.minElem)
            else:
                return print(self.stack[-1])

    def getMin(self):
        if len(self.stack) == 0:
            return print("Stack is empty")
        return print(self.minElem)


class Solution:
    # TC = O(1)
    # Sc = O(2n)
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val)
        val = min(val, (self.minStack[-1] if self.minStack else val))
        self.minStack.append(val)
        print(self.stack)

    def pop(self):
        if len(self.stack) == 0:
            return -1
        print(self.stack.pop())
        self.minStack.pop()

    def top(self):
        if len(self.stack) == 0:
            return -1
        return print(self.stack[-1])

    def getMin(self):
        if len(self.stack) == 0:
            return -1
        return print(self.minStack[-1])


# answer = MinStack()
answer = Solution()
answer.push(-2)
answer.push(0)
answer.push(-1)
answer.push(-3)
answer.push(5)
answer.push(-1)
answer.getMin()
answer.pop()
answer.pop()
answer.top()
answer.pop()
answer.getMin()
