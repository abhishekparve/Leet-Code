# Given a doubly linked list of n nodes sorted by values, the task is to remove duplicate nodes present in the linked list.

# Example 1:

# Input:
# n = 6
# 1<->1<->1<->2<->3<->4
# Output:
# 1<->2<->3<->4
# Explanation:
# Only the first occurance of node with value 1 is
# retained, rest nodes with value = 1 are deleted.

# Example 2:

# Input:
# n = 7
# 1<->2<->2<->3<->3<->4<->4
# Output:
# 1<->2<->3<->4
# Explanation:
# Only the first occurance of nodes with values 2,3 and 4 are
# retained, rest repeating nodes are deleted.
# Your Task:
# You have to complete the method removeDuplicates() which takes 1 argument: the head of the linked list.  Your function should return a pointer to a linked list with no duplicate element.

# Constraint:
# 1 <= n <= 105
# Expected Time Complexity: O(n)
# Expected Space Complexity: O(1)


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class Solution:
    def removeDuplicates(self, head):
        temp = head
        while temp and temp.next:
            nextNode = temp.next
            while nextNode and nextNode.val == temp.val:
                nextNode = nextNode.next
            temp.next = nextNode
            if nextNode:
                nextNode.prev = temp
            temp = temp.next
        return head

    def printDLL(self, head):
        curr = head
        while curr:
            print(curr.val, end="<->")
            curr = curr.next
        print("None")


answer = Solution()
head = Node(1)
head.next = Node(1)
head.next.next = Node(1)
head.next.next.next = Node(2)
head.next.next.next.next = Node(3)
head.next.next.next.next.next = Node(3)
head.next.next.next.next.next.next = Node(4)
answer.printDLL(head)
newHead = answer.removeDuplicates(head)
answer.printDLL(newHead)
