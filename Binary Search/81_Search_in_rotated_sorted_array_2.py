class Solution:
    # TC = O(log(n))
    # but if the array contains most of the elements as duplicate
    # then you are going to shrink the array by moving l and r pointer
    # In worst case you might end up shrinking nearly half of the array
    # and then you will perform the binary serach
    # Therefore the TC will be O(n/2)
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True
            # if elem at l, mid, and r are equal due to the duplicates
            # then shrink the array by incrementing l by 1 and decrementing
            # r by 1
            if nums[l] == nums[mid] and nums[mid] == nums[r]:
                l += 1
                r -= 1
                continue
            # Left sorted portion
            if nums[l] <= nums[mid]:
                # l <= target <= mid
                if nums[l] >= target and target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                # mid <= target <= r
                if nums[mid] >= target and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False


answer = Solution()
nums = [2, 5, 6, 0, 0, 1, 2]
target = 2
print(answer.search(nums, target))
