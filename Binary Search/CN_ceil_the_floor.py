class Solution:
    def ceilTheFloor(self, nums, x):
        floor = self.findFloor(nums, x)
        ceil = self.findCeil(nums, x)
        return print(f"Floor : {floor} and Ceil : {ceil}")

    def findFloor(self, nums, x):
        l = 0
        r = len(nums) - 1
        ans = -1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] < x:
                ans = nums[mid]
                l = mid + 1
            else:
                r = mid - 1
        return ans

    def findCeil(self, nums, x):
        l = 0
        r = len(nums) - 1
        ans = -1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > x:
                ans = nums[mid]
                r = mid - 1
            else:
                l = mid + 1
        return ans


answer = Solution()
nums = [3, 4, 7, 8, 8, 10]
x = 9
answer.ceilTheFloor(nums, x)
