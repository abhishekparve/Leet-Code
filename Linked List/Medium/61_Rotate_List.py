# Given the head of a linked list, rotate the list to the right by k places.

# Example 1:

# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

# Example 2:

# Input: head = [0,1,2], k = 4
# Output: [2,0,1]

# Constraints:

# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k < 0:
            return head

        len = 1
        tail = head
        while tail.next:
            tail = tail.next
            len += 1

        k = k % len
        if k % len == 0:
            return head
        temp = head
        for i in range(len - k - 1):
            temp = temp.next
        nextNode = temp.next
        temp.next = None
        tail.next = head
        newHead = nextNode
        return newHead

    def printLL(self, head):
        curr = head
        while curr:
            print(curr.val, end="->")
            curr = curr.next
        print("None")


answer = Solution()

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

answer.printLL(head)
newHead = answer.rotateRight(head, 2)
answer.printLL(newHead)
