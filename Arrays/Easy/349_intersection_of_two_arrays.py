# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must be unique and you may return the result in any order.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.

# The time complexity of this solution is O(n + m), where n is the length of nums1 and m is the length of nums2.
# This is because converting the lists to sets takes O(n) and O(m) time respectively,
# and finding the intersection of the two sets takes O(min(n, m)) time.
# Finally, converting the set back to a list takes O(min(n, m)) time as well.

# The space complexity of this solution is O(n + m),
# where n is the length of nums1 and m is the length of nums2.
# This is because creating the sets nums1 and nums2 takes O(n) and O(m) space respectively,
# and the resulting intersection set takes O(min(n, m)) space.
# Finally, converting the set back to a list takes O(min(n, m)) space as well.

class Solution:
    def intersection(self, nums1, nums2):
        nums1 = set(nums1)
        nums2 = set(nums2)
        return list(nums1 & nums2)

answer = Solution()
answer.intersection([4,9,5], [9,4,9,8,4])