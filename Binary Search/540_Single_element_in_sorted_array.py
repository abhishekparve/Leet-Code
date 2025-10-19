# https://leetcode.com/problems/single-element-in-a-sorted-array/description/


class Solution:
    def singleNonDuplicate(self, nums):
        n = len(nums)
        if len(nums) == 0:
            return nums[0]
        # If the single element is at the starting index
        if nums[0] != nums[1]:
            return nums[0]
        # If the single element is at the end
        if nums[n - 1] != nums[n - 2]:
            return nums[n - 1]

        l = 1
        r = n - 2
        while l <= r:
            mid = l + (r - l) // 2
            # if elem at mid is not equal to elem at index mid + 1 and mid - 1
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            # If you are standing at the left portion of the sorted array
            # (even, odd) == elem will be at the right side
            elif (
                mid % 2 == 0
                and nums[mid] == nums[mid + 1]
                or mid % 2 == 1
                and nums[mid] == nums[mid - 1]
            ):
                l = mid + 1
            # If you are standing at the right portion of the sorted array
            # (odd, even) == elem will be at the left side
            else:
                r = mid - 1
        return -1


# nums = [1,1,2,3,3,4,4,8,8]
# index =[0,1,2,3,4,5,6,7,8]
#       =[e,o,e,o,m,o,e,o,e]

# m = mid
# e = even
# o = odd
# before mid sequence is (even, odd), (even, odd)
# after mid sequence is (odd, even) , (odd, even)
# if index is even then the duplicate elem is next element
# if index is odd then the duplicate elem is the previous element

answer = Solution()
nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
print(answer.singleNonDuplicate(nums))
