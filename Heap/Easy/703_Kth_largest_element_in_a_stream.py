import heapq


class Solution:
    # TC = O(nlog(k) + mlog(k))
    # SC = O(n)
    def __init__(self, k, nums):
        self.k = k
        self.minHeap = nums
        # converting nums array to minHeap
        # O(n) operation
        heapq.heapify(self.minHeap)
        # if length of minHeap is greater than k then popping
        # the extra elements to ensure that the len(minHeap) == k
        # poping costs us log(n)
        # TC of init is n log(k)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    # lets say add is called M times and we are popping elements from the heap
    # if its size is greater than k which costs us log(n).
    # therefore, the TC = M * log(k)
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        # if length of minHeap is greater than k then popping
        # the extra elements to ensure that the len(minHeap) == k
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        # the top most element in minHeap is the kth largest
        return self.minHeap[0]


class SolutionBrute1:
    def __init__(self, k, nums):
        self.k = k
        self.nums = nums
        # O(nlog(n))
        self.nums.sort()

    def addBrute(self, val):
        l = 0
        r = len(self.nums) - 1
        # O(log(n)
        while l <= r:
            mid = l + (r - l) // 2
            if self.nums[mid] > val:
                r = mid - 1
            else:
                l = mid + 1
        # O(n)
        self.nums.insert(l, val)
        return self.nums[len(self.nums) - self.k]


class SolutionBrute2:
    # TC = O(nlog(n))
    def __init__(self, k, nums):
        self.k = k
        self.nums = nums

    def addBrute2(self, val):
        self.nums.append(val)
        self.nums.sort()
        self.nums[-self.k]
