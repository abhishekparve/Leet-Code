# Given the head of a linked list, return the list after sorting it in ascending order.

# Example 1:
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]

# Example 2:
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]

# Example 3:
# Input: head = []
# Output: []

# Constraints:

# The number of nodes in the list is in the range [0, 5 * 104].
# -105 <= Node.val <= 105


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def sortList(self, head):
        # Base case
        if not head or not head.next:
            return head
        # Splitting the linked list and applying mergeSort
        left = head
        mid = self.findMiddle(head)
        right = mid.next
        mid.next = None
        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)

    def findMiddle(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        return slow

    def merge(self, list1, list2):
        dummyNode = Node(0)
        temp = dummyNode
        while list1 and list2:
            if list1.val < list2.val:
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

    def printLL(self, head):
        curr = head
        while curr:
            print(curr.val, end="->")
            curr = curr.next
        print("None")


answer = Solution()
head = Node(4)
head.next = Node(2)
head.next.next = Node(1)
head.next.next.next = Node(3)
head.next.next.next.next = Node(5)

answer.printLL(head)
newHead = answer.sortList(head)
answer.printLL(newHead)
