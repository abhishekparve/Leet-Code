# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

# Note that the linked lists must retain their original structure after the function returns.

# Example 1:
# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
# Output: Intersected at '8'
# Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
# From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
# - Note that the intersected node's value is not 1 because the nodes with value 1 in A and B (2nd node in A and 3rd node in B) are different node references. In other words, they point to two different locations in memory, while the nodes with value 8 in A and B (3rd node in A and 4th node in B) point to the same location in memory.

# Example 2:
# Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
# Output: Intersected at '2'
# Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
# From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

# Example 3:
# Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# Output: No intersection
# Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
# Explanation: The two lists do not intersect, so return null.

# Constraints:

# The number of nodes of listA is in the m.
# The number of nodes of listB is in the n.
# 1 <= m, n <= 3 * 104
# 1 <= Node.val <= 105
# 0 <= skipA < m
# 0 <= skipB < n
# intersectVal is 0 if listA and listB do not intersect.
# intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.


# Follow up: Could you write a solution that runs in O(m + n) time and use only O(1) memory?


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def getIntersectionNodeOptimized(self, headA, headB):
        if not headA or not headB:
            return None
        l1 = headA
        l2 = headB
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1

    def getIntersectionNode(self, headA, headB):
        seen = set()
        l1 = headA
        l2 = headB
        while l1 or l2:
            if l1 in seen:
                return l1
            else:
                if l1:
                    seen.add(l1)
                    l1 = l1.next if l1 else None
            if l2 in seen:
                return l2
            else:
                if l2:
                    seen.add(l2)
                    l2 = l2.next if l2 else None
        return None

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

    def printLL(self, head):
        temp = head
        while temp:
            print(temp.val, end="->")
            temp = temp.next
        print("None")


answer = Solution()
head = None
head = answer.insertNode(head, 1)
head = answer.insertNode(head, 3)
head = answer.insertNode(head, 1)
head = answer.insertNode(head, 2)
head = answer.insertNode(head, 4)
head1 = head
head = head.next.next.next
headSec = None
headSec = answer.insertNode(headSec, 3)
head2 = headSec
headSec.next = head

head3 = Node(7)
head3.next = Node(8)
head3.next.next = Node(9)

print("List1: ", end="")
answer.printLL(head1)
print("List2: ", end="")
answer.printLL(head3)

# intersect = answer.getIntersectionNode(head1, head2)
intersect = answer.getIntersectionNodeOptimized(head1, head3)
answer.printLL(intersect)
if intersect == None:
    print("No intersection")
else:
    print("The intersection point is", intersect.val)
