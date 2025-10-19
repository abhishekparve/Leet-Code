class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Inserting a node at the beginning
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    # inserting the node at any position
    def insertAtIndex(self, data, index):
        position = 0
        new_node = Node(data)
        currNode = self.head
        if position == index:
            self.insertAtBegin(new_node)
        else:
            while currNode is not None and position + 1 != index:
                position = position + 1
                currNode = currNode.next
            if currNode != None:
                new_node.next = currNode.next
                currNode.next = new_node
            else:
                print("Index is not present")

    # Inserting the node at the end.
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            currNode = self.head
            while currNode.next:
                currNode = currNode.next
            currNode.next = new_node

    # Printing the Linked list
    def printLL(self):
        currNode = self.head
        if self.head is None:
            return
        else:
            while currNode:
                print(currNode.data, end="->")
                currNode = currNode.next
            print(None)

    # Deleting the node at the beginning
    def remove_first_node(self):
        if self.head is None:
            return
        self.head = self.head.next

    # Deleting last node from the Linked List
    def remove_last_node(self):
        if self.head is None:
            return
        currNode = self.head
        while currNode.next.next:
            currNode = currNode.next
        currNode.next = None

    # Deleting the node at the given index
    def remove_at_index(self, index):
        position = 0
        if position == index:
            self.remove_first_node()
        currNode = self.head
        while currNode.next is not None and position + 1 != index:
            position = position + 1
            currNode = currNode.next
        if currNode is not None:
            currNode.next = currNode.next.next
        else:
            print("Index is not present")

    # Deleting the node based on the given data
    def remove_node(self, data):
        currNode = self.head
        if currNode.data == data:
            self.remove_first_node()
        while currNode != None and currNode.next.data != data:
            currNode = currNode.next
        if currNode is None:
            return
        else:
            currNode.next = currNode.next.next


answer = LinkedList()
answer.insertAtBegin(20)
answer.insertAtBegin(30)
answer.insertAtBegin(40)
answer.insertAtBegin(50)
answer.insertAtBegin(60)
answer.printLL()
answer.insertAtEnd(100)
answer.printLL()
answer.insertAtIndex(10, 2)
answer.printLL()
answer.remove_first_node()
answer.printLL()
answer.remove_last_node()
answer.printLL()
answer.remove_at_index(2)
answer.printLL()
