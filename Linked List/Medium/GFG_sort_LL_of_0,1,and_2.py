class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def sortLLBrute(self, head):
        temp = head
        arr = []
        while temp:
            arr.append(temp.data)
            temp = temp.next
        l = 0
        r = len(arr) - 1
        i = 0
        while i <= r:
            if arr[i] == 0:
                self.swap(l, i, arr)
            elif arr[i] == 2:
                self.swap(r, i, arr)
                r -= 1
                i -= 1
            i += 1

        temp = head
        i = 0
        while temp:
            temp.data = arr[i]
            temp = temp.next
            i += 1
        return head

    def swap(self, i, j, arr):
        arr[i], arr[j] = arr[j], arr[i]

    def sortLL(self, head):
        zeroHead = Node(-1)
        oneHead = Node(-1)
        twoHead = Node(-1)
        zero = zeroHead
        one = oneHead
        two = twoHead
        temp = head
        while temp:
            if temp.data == 0:
                zero.next = temp
                zero = temp
            elif temp.data == 1:
                one.next = temp
                one = temp
            else:
                two.next = temp
                two = temp
            temp = temp.next

        zero.next = oneHead.next if oneHead.next else twoHead.next
        one.next = twoHead.next
        two.next = None
        newHead = zeroHead.next
        return newHead

    # Printing the linked list
    def printLL(self, head):
        curr = head
        while curr:
            print(curr.data, end="->")
            curr = curr.next
        print("None")


head = Node(2)
head.next = Node(1)
head.next.next = Node(0)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)
head.next.next.next.next.next = Node(0)

answer = Solution()
answer.printLL(head)
# newHead = answer.sortLLBrute(head)
newHead = answer.sortLL(head)
answer.printLL(newHead)
