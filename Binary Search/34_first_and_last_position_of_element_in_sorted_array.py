class Solution:
    def searchRange(self, nums, target):
        left = self.binarySearch(nums, target, True)
        right = self.binarySearch(nums, target, False)
        return [left, right]

    def binarySearch(self, nums, target, leftBias):
        l = 0
        r = len(nums) - 1
        i = -1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                i = mid
                if leftBias:
                    r = mid - 1
                else:
                    l = mid + 1
        return i


answer = Solution()
nums = [5, 7, 7, 8, 8, 8, 8, 8, 10]
target = 5
result = answer.searchRange(nums, target)
print(result)
