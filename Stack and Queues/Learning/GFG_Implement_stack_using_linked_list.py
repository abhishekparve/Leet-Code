# https://www.geeksforgeeks.org/problems/implement-stack-using-linked-list/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=implement-stack-using-linked-list


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def __init__(self):
        self.top_elem = None
        self.stack_size = 0

    def push(self, item):
        newNode = Node(item)
        newNode.next = self.top_elem
        self.top_elem = newNode
        self.stack_size += 1
        return self.printLL(self.top_elem)

    def pop(self):
        if self.top_elem == None:
            return print("Stack is empty")
        temp = self.top_elem
        self.top_elem = self.top_elem.next
        temp.next = None
        self.stack_size -= 1
        return print(temp.data)

    def top(self):
        if self.top_elem == None:
            return print("Stack is empty")
        return print(self.top_elem.data)

    def size(self):
        return print(self.stack_size)

    def printLL(self, temp):
        curr = temp
        while curr:
            print(curr.data, end="->")
            curr = curr.next
        print("None")


answer = Solution()
answer.push(1)
answer.push(2)
answer.push(3)
answer.pop()
answer.top()
answer.push(10)
answer.size()
answer.pop()
answer.pop()
answer.pop()
answer.pop()
