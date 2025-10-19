# You are given the head of a linked list, and an integer k.

# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [1,4,3,2,5]

# Example 2:
# Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
# Output: [7,9,6,6,8,7,3,0,9,5]

# Constraints:
# The number of nodes in the list is n.
# 1 <= k <= n <= 105
# 0 <= Node.val <= 100


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def swapNodes(self, head, k):
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next
        l = k - 1
        r = len(arr) - k
        arr[l], arr[r] = arr[r], arr[l]
        temp = head
        for n in arr:
            temp.val = n
            temp = temp.next
        return head

    def swapNodesOptimized(self, head, k):
        first = head
        last = head
        for i in range(1, k):
            first = first.next
        temp = first
        while temp.next:
            last = last.next
            temp = temp.next
        first.val, last.val = last.val, first.val
        return head

    def printLL(self, head):
        temp = head
        while temp:
            print(temp.val, end="->")
            temp = temp.next
        print("None")

    def insertNode(self, head, val):
        newNode = Node(val)
        if head is None:
            head = newNode
            return head
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = newNode
        return head


ans = Solution()
head = None
head = ans.insertNode(head, 1)
head = ans.insertNode(head, 2)
head = ans.insertNode(head, 3)
head = ans.insertNode(head, 4)
head = ans.insertNode(head, 5)
k = 2
ans.printLL(head)
ans.swapNodes(head, k)
ans.swapNodesOptimized(head, 1)
ans.printLL(head)
