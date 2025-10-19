# https://www.geeksforgeeks.org/problems/implement-queue-using-array/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=implement-queue-using-array
class Solution:
    def __init__(self):
        self.limit = 4
        self.start = -1
        self.end = -1
        self.curr_size = 0
        self.queue = [0] * self.limit

    def push(self, data):
        if self.curr_size == self.limit:
            return print("Queue is full")
        if self.curr_size == 0:
            self.start = 0
            self.end = 0
        else:
            self.end = (self.end + 1) % self.limit
        self.queue[self.end] = data
        self.curr_size += 1
        return print(self.queue)

    def pop(self):
        if self.curr_size == 0:
            return print("Queue is empty")
        pop_elem = self.queue[self.start]
        if self.curr_size == 1:
            self.start = -1
            self.end = -1
        else:
            self.start = (self.start + 1) % self.limit
        self.curr_size -= 1
        return print(pop_elem)

    # My code in python compiler
    # def push(self, data):
    #     if self.curr_size == self.limit:
    #         return print("Queue is full")
    #     if self.curr_size == 0:
    #         self.start += 1
    #         self.end += 1
    #         self.queue[self.start] = data
    #         self.curr_size += 1
    #     else:
    #         self.end = (1 + self.end) % self.limit
    #         self.queue[self.end] = data
    #         self.curr_size += 1
    #     return print(self.queue)

    # def pop(self):
    #     if self.curr_size == 0:
    #         self.start = -1
    #         self.end = -1
    #         return print("Queue is empty")
    #     x = self.queue[self.start]
    #     self.start = (1 + self.start) % self.limit
    #     self.curr_size -= 1
    #     return print(x)

    def top(self):
        if self.curr_size == 0:
            return print("Queue is empty")
        return print(self.queue[self.start])

    def size(self):
        return print(self.curr_size)


answer = Solution()
answer.push(1)
answer.push(2)
answer.push(3)
answer.pop()
answer.pop()
answer.top()
answer.size()
answer.push(4)
answer.push(5)
answer.size()
answer.push(6)
answer.push(7)
