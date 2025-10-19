class Solution:
    def findNumberOfRotations(self, nums):
        l = 0
        r = len(nums) - 1
        index = -1
        ans = float("inf")
        while l <= r:
            if nums[l] <= nums[r]:
                if nums[l] < ans:
                    index = l
                    ans = nums[l]
                    break
            mid = l + (r - l) // 2
            # Left sorted portion
            # Since we know that the nums array only contains
            # distinct integers that's why we are not adding equal(=) in
            # nums[l] < nums[mid]
            if nums[l] < nums[mid]:
                # l < ans
                if nums[l] < ans:
                    index = l
                    ans = nums[l]
                l = mid + 1
            else:
                # mid < ans
                if nums[mid] < ans:
                    index = mid
                    ans = nums[mid]
                r = mid - 1
        return index


answer = Solution()
nums = [6, 7, 9, 2, 4]
print(answer.findNumberOfRotations(nums))
