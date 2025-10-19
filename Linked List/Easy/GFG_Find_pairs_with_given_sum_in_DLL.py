# Given a sorted doubly linked list of positive distinct elements, the task is to find pairs in a doubly-linked list whose sum is equal to given value target.

# Example 1:

# Input:
# 1 <-> 2 <-> 4 <-> 5 <-> 6 <-> 8 <-> 9
# target = 7
# Output: (1, 6), (2,5)
# Explanation: We can see that there are two pairs
# (1, 6) and (2,5) with sum 7.

# Example 2:

# Input:
# 1 <-> 5 <-> 6
# target = 6
# Output: (1,5)
# Explanation: We can see that there is one pairs  (1, 5) with sum 6.

# Your Task:
# You don't need to read input or print anything. Your task is to complete the function findPairsWithGivenSum() which takes head node of the doubly linked list and an integer target as input parameter and returns an array of pairs. If there is no such pair return empty array.

# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)
# Constraints:
# 1 <= N <= 105
# 1 <= target <= 105


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class Solution:
    def findPairsBrute(self, head, target):
        if not head and not head.next:
            return head
        temp1 = head
        arr = []
        while temp1:
            temp2 = temp1.next
            while temp2 and temp1.val + temp2.val <= target:
                if temp1.val + temp2.val == target:
                    arr.append((temp1.val, temp2.val))
                temp2 = temp2.next
            temp1 = temp1.next
        return arr

    def findTail(self, head):
        curr = head
        while curr.next:
            curr = curr.next
        return curr

    def findPairsTwoPointer(self, head, target):
        if not head and not head.next:
            return head
        arr = []
        l = head
        r = self.findTail(head)
        while l.val < r.val:
            if l.val + r.val == target:
                arr.append((l.val, r.val))
                l = l.next
                r = r.prev
            elif l.val + r.val < target:
                l = l.next
            else:
                r = r.prev
        return arr

    def printDLL(self, head):
        curr = head
        while curr:
            print(curr.val, end="<->")
            curr = curr.next
        print("None")


answer = Solution()
head = Node(1)
head.next = Node(2)
head.next.next = Node(4)
head.next.next.next = Node(5)
head.next.next.next.next = Node(6)
head.next.next.next.next.next = Node(8)
head.next.next.next.next.next.next = Node(9)

answer.printDLL(head)
ans = answer.findPairsBrute(head, 7)
ans2 = answer.findPairsTwoPointer(head, 7)
print(ans)
print(ans2)
