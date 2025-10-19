class Node:
    def __init__(self, data):
        # Initializing the newNode with data, previous and next pointers
        self.data = data
        self.next = None
        self.prev = None


class DoublyLL:
    def __init__(self):
        self.head = None

    # Function to convert an array to the doubly linked list
    def convertArrayToDll(self, data):
        newNode = Node(data)
        # If head is none then make the newNode as head
        if not self.head:
            self.head = newNode
        else:
            currNode = self.head
            while currNode.next:
                currNode = currNode.next
            currNode.next = newNode
            newNode.prev = currNode

    # function to print the linked list
    def printLL(self):
        currNode = self.head
        while currNode:
            print(currNode.data, end="<->")
            currNode = currNode.next
        print("None")


answer = DoublyLL()
nums = [12, 13, 14, 15]
for n in nums:
    answer.convertArrayToDll(n)
answer.printLL()
