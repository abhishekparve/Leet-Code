# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1
# Output: []

# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def removeNodeFromEnd(head, n):
    fast = head
    slow = head
    for i in range(0, n):
        fast = fast.next

    if not fast:
        head = head.next
        return printLL(head)

    while fast.next is not None:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head


def printLL(head):
    curr = head
    while curr:
        print(curr.val, end="->")
        curr = curr.next
    print("None")


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
printLL(head)
removeNodeFromEnd(head, 5)
