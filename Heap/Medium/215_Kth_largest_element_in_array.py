import heapq


class Solution:
    # TC = O(n log(n))
    # SC = O(1)
    def kthLargestElementBrute(self, nums, k):
        nums.sort()
        # To sort in reverse
        # num2 = nums.sort(reverse=True)
        # so kth element will be at index k - 1
        return nums[len(nums) - k]

    # TC = k * log(k)
    # SC = O(k)
    def kthLargestElementHeap(self, nums, k):
        pq = []
        for i in range(len(nums)):
            heapq.heappush(pq, nums[i])
            if len(pq) > k:
                heapq.heappop(pq)

        return pq[0]

    # In quick select algorithm we are trying to build an array
    # where all the elements at the left hand side are greater than pivot
    # and the elements at right hand side are less then pivot in decending fashion
    def quickSelect(self, L, R, nums):
        i = L + 1
        j = R
        pivot = nums[L]
        while i <= j:
            if nums[i] < pivot and nums[j] > pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            if nums[i] >= pivot:
                i += 1
            if nums[j] <= pivot:
                j -= 1
        # pivot element is at the index L
        # swap the pivot element with the element at index j
        nums[L], nums[j] = nums[j], nums[L]
        # return the new pivot element at index j
        return j

    # Avg case time complexity = O(n)
    # Worst case = O(n ^ 2)
    def kthLargestElementHeapQuickSelect(self, nums, k):
        L = 0
        R = len(nums) - 1
        pivot_index = 0
        # Since we want a decending sorting, So the largest element
        # will be at the left and the smallest element will be at the right
        # Since it is decending the kth largest element will be at nums[k - 1]
        while True:
            pivot_index = self.quickSelect(L, R, nums)
            if pivot_index == k - 1:
                break
            # If we have found the 4th largest element and we are looking for 2nd largest
            # we need to look at the element at the left side so we decrement R
            elif pivot_index > k - 1:
                R = pivot_index - 1
            else:
                L = pivot_index + 1
        return nums[pivot_index]


answer = Solution()
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(answer.kthLargestElementBrute(nums, k))
print(answer.kthLargestElementHeap(nums, k))
print(answer.kthLargestElementHeapQuickSelect(nums, k))
