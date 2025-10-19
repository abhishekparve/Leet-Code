# TC = O(log(n)) and SC = O(1)


class Solution:
    def findCeil(self, nums, target):
        l = 0
        r = len(nums) - 1
        res = -1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > target:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res


answer = Solution()
nums = [1, 2, 8, 10, 11, 12, 19]
target = 13
print(answer.findCeil(nums, target))
