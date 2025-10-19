# Given the head of a singly linked list, return true if it is a
# palindrome or false otherwise.

#  Example 1:
# Input: head = [1,2,2,1]
# Output: true

# Example 2:
# Input: head = [1,2]
# Output: false

# Constraints:
# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9

# Follow up: Could you do it in O(n) time and O(1) space?


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def isPalindromeBrute(self, head):
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        l = 0
        r = len(arr) - 1
        while l <= r:
            if arr[l] != arr[r]:
                return False
            else:
                l += 1
                r -= 1
        return True

    def isPalindrome(self, head):
        # reaching to the middle of the linked list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reversing the linked list from the second middle
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # Finding the palindrome
        left = head
        right = prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

    def printLL(self, head):
        curr = head
        while curr:
            print(curr.val, end="->")
            curr = curr.next
        print("None")


head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(1)

answer = Solution()
answer.printLL(head)
value = answer.isPalindrome(head)
print(value)
answer.printLL(head)
value2 = answer.isPalindromeBrute(head)
print(answer.isPalindromeBrute(head))
