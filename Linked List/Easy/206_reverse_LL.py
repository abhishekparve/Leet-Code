# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = [1,2]
# Output: [2,1]

# Example 3:
# Input: head = []
# Output: []

# Constraints:
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000

# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

# METHOD :Recursive


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_linked_list(head):
    if head is None or head.next is None:
        return head

    new_head = reverse_linked_list(head.next)

    front = head.next
    front.next = head
    head.next = None
    return new_head


def reverse_iterative(head):
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


# Function to print the linked list
def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end="->")
        temp = temp.next
    print("None")


# Create a linked list with
# values 1, 3, 2, and 4
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

# Print the original linked list
print("Original Linked List:", end=" ")
print_linked_list(head)

# Reverse the linked list
# head = reverse_linked_list(head)
head = reverse_iterative(head)

# Print the reversed linked list
print("Reversed Linked List:", end=" ")
print_linked_list(head)
