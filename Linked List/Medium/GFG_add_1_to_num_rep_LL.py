# A number n is represented in Linked List such that each digit corresponds to a node in linked list. You need to add 1 to it. Returns the head of the modified linked list. The driver code prints the number.

# Note: The head represents the left-most digit of the number.

# Examples :

# Input: LinkedList: 4->5->6
# Output: 457
# Explanation: 4->5->6 represents 456 and when 1 is added it becomes 457.
# Input: LinkedList: 1->2->3
# Output: 124
# Explanation:  1->2->3 represents 123 and when 1 is added it becomes 124.
# Expected Time Complexity: O(n).
# Expected Auxiliary Space: O(1).

# Constraints:
# 1 <= n <= 1021


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    # TC = O(3n) SC = O(1)
    def iterativeAddition(self, head):
        # Reversing the linked list
        head = self.reverse(head)
        temp = head
        carry = 1
        while temp:
            sum = temp.data + carry
            if sum < 10:
                temp.data = sum
                carry = 0
                break
            else:
                temp.data = 0
                carry = 1
            temp = temp.next
        # Reversing the linked list
        head = self.reverse(head)
        if carry == 1:
            newHead = Node(carry)
            newHead.next = head
            return newHead
        return head

    # Recursive approach
    def recursiveAddition(self, head):
        carry = self.helper(head)
        if carry == 1:
            newHead = Node(carry)
            newHead.next = head
            return newHead
        return head

    def helper(self, temp):
        if temp is None:
            return 1
        carry = self.helper(temp.next)
        temp.data = temp.data + carry
        if temp.data < 10:
            return 0
        else:
            temp.data = 0
            return 1

    # function for reversing a linked list
    def reverse(self, head):
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    # Printing the linked list
    def printLL(self, head):
        curr = head
        while curr:
            print(curr.data, end="->")
            curr = curr.next
        print("None")


head = Node(9)
head.next = Node(9)
head.next.next = Node(9)
answer = Solution()
answer.printLL(head)
# newHead = answer.iterativeAddition(head)
newHead = answer.recursiveAddition(head)
answer.printLL(newHead)
