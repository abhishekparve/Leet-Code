# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Constraints:
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.


# TC and SC = O(max(l1, l2))
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def addTwoNumbers(l1, l2, dummyNode):
    # dummyNode = Node(-1)
    curr = dummyNode
    carry = 0
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        value = v1 + v2 + carry
        carry = value // 10
        value = value % 10
        curr.next = Node(value)
        # incrementing the pointers
        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummyNode.next


# Function to print the linked list
def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.val, end="->")
        temp = temp.next
    print("None")


# Create a linked list with
# values 1, 3, 2, and 4
l1 = Node(2)
l1.next = Node(4)
l1.next.next = Node(3)
print_linked_list(l1)
l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(4)
print_linked_list(l2)
dummyNode = Node(-1)
addTwoNumbers(l1, l2, dummyNode)
print_linked_list(dummyNode.next)
