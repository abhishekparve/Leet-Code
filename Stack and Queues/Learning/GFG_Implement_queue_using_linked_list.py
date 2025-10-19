class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def __init__(self):
        self.queue_size = 0
        self.start = None
        self.end = None

    def printLL(self, temp):
        curr = temp
        while curr:
            print(curr.data, end="->")
            curr = curr.next
        print("None")

    def push(self, item):
        newNode = Node(item)
        if self.queue_size == 0:
            self.start = newNode
            self.end = newNode
        else:
            self.end.next = newNode
            self.end = newNode
        self.queue_size += 1
        return self.printLL(self.start)

    def pop(self):
        if self.queue_size == 0:
            self.start = None
            self.end = None
            return print("Queue is empty")
        pop_elem = self.start
        self.start = self.start.next
        self.queue_size -= 1
        return print(pop_elem.data)

    def top(self):
        if self.queue_size == 0:
            return print("Queue ie empty")
        return print(self.start.data)

    def size(self):
        return print(self.queue_size)


answer = Solution()
answer.push(1)
answer.push(2)
answer.push(3)
answer.top()
answer.pop()
answer.size()
answer.push(4)
