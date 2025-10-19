# 1. Insertion at the Beginning
# 2. Insertion after the given node
# 3. Insertion before the given node
# 4. Insertion at the end


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def insert_at_the_beginning(head, data):
    newNode = Node(data)
    newNode.next = head
    if head:
        head.prev = newNode
    return newNode


def insert_after_node(head, node, data):
    if node is None:
        print("Error : The given node is none")
        return
    newNode = Node(data)
    newNode.prev = node
    newNode.next = node.next
    if node.next:
        node.next.prev = newNode
    node.next = newNode
    return head


def insert_before_node(head, node, data):
    if node is None:
        print("Error : The given node is none")
        return
    newNode = Node(data)
    newNode.next = node
    newNode.prev = node.prev
    if node.prev:
        node.prev.next = newNode
    node.prev = newNode
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
    return head


def delete_at_beginning(head):
    if head is None:
        print("Error: Doubly Linked List is empty")
        return None
    if head.next is None:
        return None
    new_head = head.next
    new_head.prev = None
    del head
    return new_head


def printLL(head):
    currNode = head
    while currNode:
        print(currNode.data, end="->")
        currNode = currNode.next
    print("None")


# Diver code for inserting at the beginning
# head = None
# head = insert_at_the_beginning(head,3)
# head = insert_at_the_beginning(head,2)
# head = insert_at_the_beginning(head,1)

# Driver code for inserting after a given node
# head = Node(1)
# node2 = Node(2)
# node3 = Node(3)

# head.next = node2
# node2.prev = head
# node2.next = node3
# node3.prev = node2

# Inserting the new node at the end of the DLL
# head = None
# head = insert_at_end(head, 1)
# head = insert_at_end(head, 2)
# head = insert_at_end(head, 3)
# head = insert_at_end(head, 4)
# printLL(head)
# head = insert_after_node(head, node2, 4)
# head = insert_before_node(head, node2, 6)
# head = insert_before_node(head, node3, 8)
# printLL(head)
