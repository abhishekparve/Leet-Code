# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

# Example 2:
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

# Constraints:
# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# looping over all the nodes and finding length. Then run the next loop half the length of the list.
# In this approach we are iterating the LL two times
def middleOfLLApproach1(head):
    if head is None or head.next is None:
        return head
    temp = head
    length = 0
    while temp:
        temp = temp.next
        length += 1
    n = length // 2
    mid = head
    for i in range(0, n):
        mid = mid.next
    head = mid
    return head


# Optimized approach
# Move the fast pointer by two steps and slow poiunter by one step
# when fast or fast.next becomes null return slow
def middleOfLLTwoPointer(head):
    fast = head
    slow = head
    #  Here is one tricky part, while giving condition of loop
    #  For list with even length, fast pointer is going to reach end i.e. null
    #  For off length, fast pointer is going to be at the tail
    #  so we have to terminate the loop
    #  if fast becomes null && fast.next becomes null
    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next
    return slow


def printLL(head):
    curr = head
    while curr:
        print(curr.data, end="->")
        curr = curr.next
    print("None")


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
printLL(head)
mid = middleOfLLApproach1(head)
printLL(mid)
mid = middleOfLLTwoPointer(head)
printLL(mid)
