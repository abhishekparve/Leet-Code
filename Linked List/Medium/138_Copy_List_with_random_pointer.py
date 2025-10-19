# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

# Return the head of the copied linked list.

# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.

# Example 1:
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

# Example 2:
# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]

# Example 3:
# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]

# Constraints:

# 0 <= n <= 1000
# -104 <= Node.val <= 104
# Node.random is null or is pointing to some node in the linked list.


class Node:
    def __init__(self, val, random=None):
        self.val = val
        self.random = random
        self.next = None


class Solution:
    def insertingNodesInBetween(self, head):
        temp = head
        while temp:
            copyNode = Node(temp.val)
            copyNode.next = temp.next
            temp.next = copyNode
            temp = temp.next.next

    def connectingRandomPointers(self, head):
        temp = head
        while temp:
            copyNode = temp.next
            if temp.random:
                copyNode.random = temp.random.next
            else:
                copyNode.random = None
            temp = temp.next.next

    def getDeepCopyList(self, head):
        temp = head
        dummyNode = Node(-1)
        res = dummyNode

        while temp:
            res.next = temp.next
            res = res.next
            temp.next = temp.next.next
            temp = temp.next

        return dummyNode.next

    def copyRandomListOptimal(self, head):
        if not head:
            return head

        self.insertingNodesInBetween(head)
        self.connectingRandomPointers(head)
        copiedList = self.getDeepCopyList(head)
        return copiedList

    def copyRandomListBrute(self, head):
        map = {}
        temp = head
        while temp is not None:
            copyNode = Node(temp.val)
            map[temp] = copyNode
            temp = temp.next

        temp = head
        while temp is not None:
            copyNode = map[temp]
            copyNode.next = map.get(temp.next)
            copyNode.random = map.get(temp.random)
            temp = temp.next
        return map[head]

    def printLL(self, head):
        curr = head
        while curr:
            print(curr.val, end="->")
            if curr.random is not None:
                print(f", Random: {curr.random.val}")
            else:
                print(", Random: nullptr")
            curr = curr.next
        print("None")


answer = Solution()
head = Node(7)
head.next = Node(14)
head.next.next = Node(21)
head.next.next.next = Node(28)

# Assigning random pointers
head.random = head.next.next
head.next.random = head
head.next.next.random = head.next.next.next
head.next.next.next.random = head.next

print("Original Linked List with Random Pointers:")
answer.printLL(head)
print("Copied Linked List with Random Pointers:")
# newLL = answer.copyRandomListBrute(head)
newLL = answer.copyRandomListOptimal(head)
answer.printLL(newLL)
