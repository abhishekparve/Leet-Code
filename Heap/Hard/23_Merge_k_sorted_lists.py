import heapq


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    # TC = O(n log(n))
    def mergeKListsBrute(self, lists):
        result = []
        for i in range(len(lists)):
            temp = lists[i]
            while temp:
                result.append(temp.val)
                temp = temp.next
        # Sort the result
        result.sort()
        # create a dummy node
        dummy = ListNode()
        temp = dummy
        #
        for num in result:
            temp.next = ListNode(num)
            temp = temp.next
        return dummy.next

    # TC = O(N log(k))
    # N is the total length of each linked list - worst case
    # O(log k) - Recursive call stack
    def merge(self, l1, l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val <= l2.val:
            l1.next = self.merge(l1.next, l2)
            return l1
        else:
            l2.next = self.merge(l1, l2.next)
            return l2

    def partitionAndMerge(self, start, end, lists):
        if start > end:
            return None
        if start == end:
            return lists[start]
        mid = start + (end - start) // 2
        L1 = self.partitionAndMerge(start, mid, lists)
        L2 = self.partitionAndMerge(mid + 1, end, lists)
        return self.merge(L1, L2)

    def mergeKLists(self, lists):
        k = len(lists)
        if k == 0:
            return None
        start = 0
        end = k - 1
        return self.partitionAndMerge(start, end, lists)

    def mergeKListsHeap(self, lists):
        if not lists:
            return None
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        current = dummy
        while heap:
            val, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next

    def printLL(self, head):
        temp = head
        while temp:
            print(temp.val, end="->")
            temp = temp.next
        return print("None")

    def createNewList(self):
        head1 = ListNode(1)
        head1.next = ListNode(4)
        head1.next.next = ListNode(5)

        head2 = ListNode(1)
        head2.next = ListNode(3)
        head2.next.next = ListNode(4)

        head3 = ListNode(2)
        head3.next = ListNode(6)

        lists = [head1, head2, head3]
        return lists


answer = Solution()
head1 = ListNode(1)
head1.next = ListNode(4)
head1.next.next = ListNode(5)

head2 = ListNode(1)
head2.next = ListNode(3)
head2.next.next = ListNode(4)

head3 = ListNode(2)
head3.next = ListNode(6)

lists = []
lists.append(head1)
lists.append(head2)
lists.append(head3)

lists2 = [head1, head2, head3]

print("\nMerge using divide and conquer:")
lists1 = answer.createNewList()
merged_head = answer.mergeKLists(lists1)
answer.printLL(merged_head)

print("\nMerge using heap:")
lists2 = answer.createNewList()
heap_merged_head = answer.mergeKListsHeap(lists2)
answer.printLL(heap_merged_head)
