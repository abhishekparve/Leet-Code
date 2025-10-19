from operator import itemgetter
import heapq


class Solution:
    # TC = O(nlog(n))
    def topKFrequentBrute(self, nums, k):
        freq_map = {}
        for i in range(len(nums)):
            freq_map[nums[i]] = freq_map.get(nums[i], 0) + 1

        result = []
        for key, val in freq_map.items():
            result.append((key, val))

        # using itemgetter to sort based on val
        result.sort(key=itemgetter(1), reverse=True)

        res = []
        for i in range(k):
            res.append(result[i][0])
        return res

    # We are talking about frequency here where we want to return
    # elements with greater freq. In this case, if we use a heap we
    # want to get the element with greater freq at the top
    # Which means we want to pop the elements with lower freq in O(1)
    # so here min-heap has the elements with low freq at top which can be easily
    # popped. Therefore we go for min-heap
    # TC = O(n log(k))
    # Sc = O(3n)
    def topKFrequentHeap(self, nums, k):
        min_heap = []
        result = []
        freq_map = {}
        for i in range(len(nums)):
            freq_map[nums[i]] = freq_map.get(nums[i], 0) + 1

        for key, val in freq_map.items():
            heapq.heappush(min_heap, (val, key))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        while min_heap:
            val, key = heapq.heappop(min_heap)
            result.append(key)
        return result

    # TC = O(n)
    # SC = O(2n)
    def topKFrequentUsingBucketSort(self, nums, k):
        freq_count = {}
        # maintaining a frequency count of each element using hash map
        for i in range(len(nums)):
            freq_count[nums[i]] = freq_count.get(nums[i], 0) + 1

        # We need bucket size of len(nums) because at max an element can be repeated
        # n times, where n is len(nums)
        bucket = [[] for i in range(len(nums) + 1)]

        # count = index (which denotes the freq count of elements in bucket and it also
        #                represents the index in the bucket list)
        # key = element
        # bucket[count] = represents the list of elements having that "count(index)" as the frequency
        for key, count in freq_count.items():
            bucket[count].append(key)

        result = []
        # iterating over the bucket list in reverse order because
        # since here the index represent the freq count of the elements
        # So the elements having the greater freq_count will be towards the right
        for i in range(len(bucket) - 1, -1, -1):
            if len(bucket[i]) == 0:
                continue
            # iterating over each elem in bucket[i]
            for val in bucket[i]:
                result.append(val)
                if len(result) == k:
                    return result


answer = Solution()
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(answer.topKFrequentBrute(nums, k))
print(answer.topKFrequentHeap(nums, k))
print(answer.topKFrequentUsingBucketSort(nums, k))
