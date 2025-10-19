# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/
import math


# TC = O(log(max(nums)) * N)
class Solution:
    def calculateSum(self, nums, mid):
        total = 0
        for i in range(len(nums)):
            total += math.ceil(nums[i] / mid)
        return total

    def findSmallestDivisor(self, nums, threshold):
        l = 1
        r = max(nums)
        res = 0
        while l <= r:
            mid = l + (r - l) // 2
            total_sum = self.calculateSum(nums, mid)
            if total_sum < threshold:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res


answer = Solution()
nums = [1, 2, 5, 9]
threshold = 6
print(answer.findSmallestDivisor(nums, threshold))
