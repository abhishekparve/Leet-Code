# Delete at the beginning
# Delete at the end
# Delete at a position


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def delete_at_beginning(head):
    if head is None:
        print("Error: Doubly Linked List is empty")
        return None
    if head.next is None:
        return None
    newHead = head.next
    newHead.prev = None
    del head
    return newHead


def delete_at_end(head):
    if head is None:
        print("Error: Doubly Linked List is empty")
        return None
    currNode = head
    while currNode.next.next:
        currNode = currNode.next
    currNode.next = None
    return currNode


def delete_at_position(head, position):
    if head is None:
        print("Doubly Linked List is empty")
        return None
    if position < 0:
        print("invalid Position")
        return head
    if position == 0:
        if head.next:
            head.nex.prev = None
        return head.next

    currNode = head
    count = 0
    while currNode and count < position:
        currNode = currNode.next
        count += 1
    if currNode is Node:
        print("Position out of range")
        return head
    if currNode.next:
        currNode.next.prev = currNode.prev
    if currNode.prev:
        currNode.prev.next = currNode.next
    del currNode
    return head


def insert_at_end(head, data):
    newNode = Node(data)
    if not head:
        head = newNode
    else:
        currNode = head
        while currNode.next:
            currNode = currNode.next
        currNode.next = newNode
        newNode.prev = currNode
        newNode.next = None
    return head


def printLL(head):
    currNode = head
    while currNode:
        print(currNode.data, end="<->")
        currNode = currNode.next
    print("None")


# Deleting the node at the beginning
head = None
head = insert_at_end(head, 11)
head = insert_at_end(head, 12)
head = insert_at_end(head, 13)
head = insert_at_end(head, 14)
# printLL(head)
# head = delete_at_beginning(head)
# printLL(head)
# head = delete_at_end(head)
head = delete_at_position(head, 2)
printLL(head)
