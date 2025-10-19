import heapq


class Solution:
    # TC = O(n × m × log(n × m))
    def findMaxSumBrute(self, nums1, nums2, k):
        result = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                result.append(nums1[i] + nums2[j])

        result.sort(reverse=True)
        return result[:k]

    # TC = O(n x m x log(n x m) + klog(n x m))
    def findMaxSumHeap(self, nums1, nums2, k):
        result = []
        max_heap = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                pair_sum = nums1[i] + nums2[j]
                heapq.heappush(max_heap, -pair_sum)

        while k and max_heap:
            val = -heapq.heappop(max_heap)
            result.append(val)
            k -= 1
        return result

    # TC = O(n x m x log(k) + k log(k))
    def findMaxSumHeapOptimized(self, nums1, nums2, k):
        result = []
        min_heap = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                pair_sum = nums1[i] + nums2[j]
                if len(min_heap) < k:
                    heapq.heappush(min_heap, pair_sum)
                elif pair_sum > min_heap[0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, pair_sum)

        while k and min_heap:
            val = heapq.heappop(min_heap)
            result.append(val)
            k -= 1

        result.sort(reverse=True)
        return result


answer = Solution()
nums1 = [1, 4, 2, 3]
nums2 = [2, 5, 1, 6]
k = 3
print(answer.findMaxSumBrute(nums1, nums2, k))
print(answer.findMaxSumHeap(nums1, nums2, k))
print(answer.findMaxSumHeapOptimized(nums1, nums2, k))
