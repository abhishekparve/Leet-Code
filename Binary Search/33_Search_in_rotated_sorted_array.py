# https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution:
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            # Left Sorted Portion
            # Check if it statisfies the basic binary search condition for left portion
            # i.e, elem at left most position will always be less than the mid
            if nums[l] <= nums[mid]:
                # l <= target <= mid
                if target >= nums[l] and target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # Right sorted portion
            else:
                # mid <= target <= r
                if target >= nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


answer = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
target = 10
result = answer.search(nums, target)
print(result)
