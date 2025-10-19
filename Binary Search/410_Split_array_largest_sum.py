# https://leetcode.com/problems/split-array-largest-sum/description/


class Solution:
    # TC = O(sum - max + 1)*O(n)
    def splitArrayLargestSumBrute(self, nums, k):
        start = max(nums)
        end = sum(nums)
        for i in range(start, end + 1):
            min_splits = self.computeSplit(nums, i)
            if min_splits == k:
                return i
        return start

    # TC = O(log(sum - max + 1)*O(n))
    def splitArrayLargestSumOptimal(self, nums, k):
        l = max(nums)
        r = sum(nums)
        while l <= r:
            mid = l + (r - l) // 2
            min_splits = self.computeSplit(nums, mid)
            if min_splits > k:
                l = mid + 1
            else:
                r = mid - 1
        return l

    def computeSplit(self, nums, maxSum):
        k = 1
        sum_of_subarray = 0
        for i in range(len(nums)):
            if sum_of_subarray + nums[i] <= maxSum:
                sum_of_subarray += nums[i]
            else:
                k += 1
                sum_of_subarray = nums[i]
        return k


answer = Solution()
nums = [7, 2, 5, 10, 8]
k = 2
print(answer.splitArrayLargestSumBrute(nums, k))
print(answer.splitArrayLargestSumOptimal(nums, k))
