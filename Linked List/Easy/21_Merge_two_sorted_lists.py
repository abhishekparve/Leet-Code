# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]

# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def mergeTwoLists(list1, list2):
    dummyNode = Node(0)
    temp = dummyNode
    while list1 and list2:
        if list1.data < list2.data:
            temp.next = list1
            temp = list1
            list1 = list1.next
        else:
            temp.next = list2
            temp = list2
            list2 = list2.next

    if list1:
        temp.next = list1
    elif list2:
        temp.next = list2

    return dummyNode.next


def printLL(head):
    curr = head
    while curr:
        print(curr.data, end="->")
        curr = curr.next
    print("None")


list1 = Node(1)
list1.next = Node(2)
list1.next.next = Node(4)
print("Linked List : 1")
printLL(list1)

list2 = Node(1)
list2.next = Node(3)
list2.next.next = Node(4)
print("Linked List : 2")
printLL(list2)

print("After merge of Linked List")
head = mergeTwoLists(list1, list2)
printLL(head)
