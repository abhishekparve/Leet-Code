import heapq


class MedianFinder:
    # TC = O(logn)
    # SC = O(2n)
    def __init__(self):
        # Max heap for the lower half of numbers
        self.left_max_heap = []
        # Min heap for the upper half of numbers
        self.right_min_heap = []

    def addNum(self, num: int) -> None:
        # if left max heap is empty or the current number is less than
        # the top element of the left max heap push that number to left max heap
        if len(self.left_max_heap) == 0 or (num) <= -self.left_max_heap[0]:
            heapq.heappush(self.left_max_heap, -1 * num)
        else:
            heapq.heappush(self.right_min_heap, num)

        # Balancing the heaps so that the size difference is not more than 1
        # if left max heap has 2 more elements than right min heap
        # then pop the element from left and push it in right
        # below if condition, you can also write as
        # abs(len(self.left_max_heap) - len(self.right_min_heap)) > 1

        if len(self.left_max_heap) > len(self.right_min_heap) + 1:
            val = -heapq.heappop(self.left_max_heap)
            heapq.heappush(self.right_min_heap, val)
        # if the length of the right min heap is greater than left max heap
        # then pop the element from the right and push it to left
        elif len(self.left_max_heap) < len(self.right_min_heap):
            val = heapq.heappop(self.right_min_heap)
            heapq.heappush(self.left_max_heap, -val)

    def findMedian(self) -> float:
        # even - case
        if len(self.left_max_heap) == len(self.right_min_heap):
            med = (-self.left_max_heap[0] + self.right_min_heap[0]) / 2
            return med
        # odd - case
        # In this case the median will always be at the left max heap
        # because we are ensursing that the left side will always
        # have one extra element than the right
        else:
            return -self.left_max_heap[0]


class Solution:
    # Brute force
    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.nums.sort()

    def findMedian(self) -> float:
        n = len(self.nums)
        if n % 2:
            return self.nums[n // 2]
        else:
            a = (n - 1) // 2
            b = n // 2
            med = (self.nums[a] + self.nums[b]) / 2
            return med


medianFinder = MedianFinder()
medianFinder.addNum(1)
# arr = [1]
medianFinder.addNum(2)
# arr = [1, 2]
medianFinder.findMedian()
# return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3)
# arr[1, 2, 3]
medianFinder.findMedian()
# return 2.0
