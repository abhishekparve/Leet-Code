class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLL:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insert_at_end(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            return
        currNode = self.head
        while currNode:
            currNode = currNode.next
        currNode.next = newNode

    def printLL(self):
        currNode = self.head
        while currNode:
            print(currNode.data, end="->")
            currNode = currNode.next
        print("None")


answer = CircularLL()
# answer.insert_at_beginning(14)
# answer.insert_at_beginning(13)
# answer.insert_at_beginning(12)
# answer.insert_at_beginning(11)
answer.insert_at_end(12)
answer.insert_at_end(13)
answer.insert_at_end(14)
answer.insert_at_end(15)
answer.printLL()
