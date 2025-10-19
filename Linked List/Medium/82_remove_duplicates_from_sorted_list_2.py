class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# TC = O(n) SC = O(1)
class Solution:
    def removeDuplicates(self, head):
        dummyNode = Node(0)
        prev = dummyNode
        dummyNode.next = head
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                while curr and curr.next and curr.val == curr.next.val:
                    curr = curr.next
                curr = curr.next
                prev.next = curr
            else:
                prev = prev.next
                curr = curr.next
        return dummyNode.next

    def printLL(self, head):
        curr = head
        while curr:
            print(curr.val, end="->")
            curr = curr.next
        print("None")


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(3)
head.next.next.next.next = Node(4)
head.next.next.next.next.next = Node(4)
head.next.next.next.next.next.next = Node(5)
head.next.next.next.next.next.next.next = Node(6)

answer = Solution()
answer.printLL(head)
newHead = answer.removeDuplicates(head)
answer.printLL(newHead)
