# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/


class Solution:
    def findMinimum(self, nums):
        l = 0
        r = len(nums) - 1
        min_res = float("inf")
        while l <= r:
            # if elem at l is less than elem at r
            # then we can exit the binary search early
            # because the elem at l will be our minimum
            if nums[l] < nums[r]:
                min_res = min(min_res, nums[l])
                break
            mid = l + (r - l) // 2
            # Left sorted portion condition
            if nums[l] <= nums[mid]:
                min_res = min(min_res, nums[l])
                l = mid + 1
            else:
                min_res = min(min_res, nums[mid])
                r = mid - 1
        return min_res


answer = Solution()
nums = [3, 4, 5, -1, 2]
print(answer.findMinimum(nums))
