import heapq
from operator import itemgetter


class Solution:
    # Brute force
    # TC = O(n^2log(k) + klog(k))
    def findMaxSumBrute(self, nums1, nums2, k):
        # Both the arrays have same length
        n = len(nums1)
        result = [0] * n
        min_heap = []
        # Iterating over each elem in array to find the smaller
        # elem that the current one
        for i in range(len(nums1)):  # O(n)
            for j in range(len(nums1)):  # O(n)
                if nums1[j] < nums1[i]:
                    # Adding the element in the minHeap
                    heapq.heappush(min_heap, nums2[j])  # ---log(k) push and pop
                # If the minHeap size exceeds than k
                # then poping the elem from the heap
                # purpose of using min_heap is because we can easily eliminated
                # smaller elements from the top
                if len(min_heap) > k:
                    heapq.heappop(min_heap)
            total = 0
            # popping all the elements from the min_heap and adding to the total
            # k log(k)
            while min_heap:
                total += heapq.heappop(min_heap)
            # assing total value at result[i]
            result[i] = total
        return result

    # 1. Add the elements in temp array in this fashion (nums1, index, nums2) indexes = [0 , 1, 2]
    # 2. Sort the temp array (Sorting is helping here to save the second O(n) operation in the above
    #    brute force solution)
    #    Here the advantage of sorting is that we know that the elements that are
    #    smaller than the current element will always be towards the left and that why we have included
    #    (nums1, index, nums2) in the temp array. So we can easily check the elements
    #     smaller than the current num1 element and access the value of num2 along
    #     with the exact index.
    # 3. Iterate over the temp array and calculate the sum and also append the same sum in the
    #    min-heap.
    # 4. If min-heap exceeds the k threshold pop that element and also subtract the popped
    #    element from the sum
    # EDGE CASE : if we have a case [1, 1, 2, 3], here both the 1's have no element smaller than
    # itself. With the help of the first logic we would have appended "0" at index i in result array
    # but now when it comes to populating the result[i] for the second 1.
    # We will just check what value was previously filled for the earlier 1.
    # So that we can store the exact same value for the second 1 at index i in result array.
    # TC = O(n) + O(nlog(n)) + O(nlog(k))
    def findMaxSum(self, nums1, nums2, k):
        n = len(nums1)
        result = [0] * n
        temp = []  # (nums1, index, nums2)
        min_heap = []
        for i in range(n): # O(n)
            temp.append((nums1[i], i, nums2[i]))

        # sorting based on nums1 elem at index 0
        temp.sort(key=itemgetter(0)) # --- O(nlog(n))
        total = 0
        for i in range(len(temp)): # --- O(nlog(k))
            # checking the nums1 value for the current and the previous index
            # in the temp array. temp[i - 1][0] will return you nums1 value at index i - 1
            # and temp[i][0] will return you the nums1 value at index i
            if i > 0 and temp[i - 1][0] == temp[i][0]:
                # temp[i - 1][1] will return you the index of the previous "1" value
                val = result[temp[i - 1][1]]
                result[temp[i][1]] = val
            else:
                result[temp[i][1]] = total

            # temp[i][2] will return you the num2 value of the temp at index i
            # adding the num2 value to the total
            total += temp[i][2]
            # adding the num2 value in the heap
            heapq.heappush(min_heap, temp[i][2])
            if len(min_heap) > k:
                total -= heapq.heappop(min_heap)

        return result


answer = Solution()
nums1 = [4, 2, 1, 5, 3]
nums2 = [10, 20, 30, 40, 50]
k = 2
print(answer.findMaxSum(nums1, nums2, k))
