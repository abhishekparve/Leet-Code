# https://leetcode.com/problems/find-peak-element/description/


# TC = O(log(n)) and SC = O(1)
class Solution:
    def findPeak(self, nums):
        n = len(nums) - 1
        # If array has only one element
        if len(nums) == 1:
            return 0
        # If the first element of an array is the peak
        if nums[0] > nums[1]:
            return 0
        # If the last element of an array is the peak
        if nums[n - 1] > nums[n - 2]:
            return n - 1
        l = 1
        r = n - 2
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            # mid present in the increasing curve
            elif nums[mid] > nums[mid - 1]:
                l = mid + 1
            # you can simply right the else condition of r = mid - 1. The condition
            # will take care of mid present in the decreasing curve as well as array
            # having multiple peaks.
            # the additional else is written just in case if you have more than one
            # peaks and you have used an elseif condition for decresing curve check.
            # In such case either you can go to the left or you can go to the
            # right. It doesn't matter
            elif nums[mid] > nums[mid + 1]:
                r = mid - 1
            else:
                l = mid + 1
        return -1


answer = Solution()
nums = [1, 2, 1, 3, 5, 6, 4]
print(answer.findPeak(nums))
