# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]

# Example 2:
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]

# Constraints:

# The number of nodes in the list is n.
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000

# Follow-up: Can you solve the problem in O(1) extra memory space?


# TC = O(n)and SC = O(1)
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def reverse(self, head):
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def getKthNode(self, head, k):
        temp = head
        k -= 1
        while temp and k > 0:
            temp = temp.next
            k -= 1
        return temp

    def reverseKGroup(self, head, k):
        temp = head
        while temp:
            kthNode = self.getKthNode(temp, k)
            if kthNode is None:
                if prevLast:
                    prevLast.next = temp
                    return head
            nextNode = kthNode.next
            kthNode.next = None
            self.reverse(temp)
            if head == temp:
                head = kthNode
            else:
                prevLast.next = kthNode
            prevLast = temp
            temp = nextNode
        return head

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
updatedList = answer.reverseKGroup(head, 2)

answer.printLL(updatedList)
