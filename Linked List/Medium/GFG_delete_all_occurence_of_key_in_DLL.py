# You are given the head_ref of a doubly Linked List and a Key. Your task is to delete all occurrences of the given key if it is present and return the new DLL.

# Example1:

# Input:
# 2<->2<->10<->8<->4<->2<->5<->2
# 2
# Output:
# 10<->8<->4<->5
# Explanation:
# All Occurences of 2 have been deleted.

# Example2:

# Input:
# 9<->1<->3<->4<->5<->1<->8<->4
# 9
# Output:
# 1<->3<->4<->5<->1<->8<->4
# Explanation:
# All Occurences of 9 have been deleted.
# Your Task:

# Complete the function void deleteAllOccurOfX(struct Node** head_ref, int key), which takes the reference of the head pointer and an integer value key. Delete all occurrences of the key from the given DLL.

# Expected Time Complexity: O(N).

# Expected Auxiliary Space: O(1).

# Constraints:

# 1<=Number of Nodes<=105

# 0<=Node Value <=109


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class Solution:
    def deleteAllOccurence(se1f, head, key):
        temp = head
        while temp:
            if temp.val == key:
                if temp == head:
                    head = temp.next
                nextNode = temp.next
                prevNode = temp.prev
                if nextNode:
                    nextNode.prev = prevNode
                if prevNode:
                    prevNode.next = nextNode
                temp = nextNode
            else:
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
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(3)
head.next.next.next.next = Node(4)
head.next.next.next.next.next = Node(4)
head.next.next.next.next.next.next = Node(5)
head.next.next.next.next.next.next.next = Node(6)

answer.printDLL(head)
key = 3
newHead = answer.deleteAllOccurence(head, key)
answer.printDLL(newHead)
