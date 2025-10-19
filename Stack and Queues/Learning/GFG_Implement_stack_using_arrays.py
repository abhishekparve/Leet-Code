# https://www.geeksforgeeks.org/problems/implement-stack-using-array/1?utm_source=youtube
class Solution:
    def __init__(self):
        self.stack_size = 10
        self.top_elem = -1
        self.arr = [0] * self.stack_size

    def push(self, data):
        self.top_elem += 1
        self.arr[self.top_elem] = data
        return print(self.arr)

    def pop(self):
        if self.top_elem == -1:
            return -1
        else:
            x = self.arr[self.top_elem]
            self.top_elem -= 1
            return print(x)

    def top(self):
        if self.top_elem == -1:
            return -1
        else:
            return print(self.arr[self.top_elem])

    def size(self):
        return print(self.top_elem + 1)


answer = Solution()
answer.push(1)
answer.push(2)
answer.push(3)
answer.top()
answer.pop()
answer.size()
answer.top()
answer.push(4)
answer.size()
