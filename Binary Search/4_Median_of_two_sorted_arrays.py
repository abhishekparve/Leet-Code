# https://leetcode.com/problems/median-of-two-sorted-arrays/


class Solution:
    # Brute
    # TC = O(m + n)
    # SC = O(m +n)
    def findMedianSortedArraysBrute(self, nums1, nums2):
        i = 0
        j = 0
        temp = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                temp.append(nums1[i])
                i += 1
            else:
                temp.append(nums2[j])
                j += 1

        while i < len(nums1):
            temp.append(nums1[i])
            i += 1

        while j < len(nums2):
            temp.append(nums2[j])
            j += 1

        if len(temp) % 2 == 0:
            a = len(temp) // 2
            b = len(temp) // 2 - 1
            return (temp[a] + temp[b]) / 2
        else:
            a = len(temp) // 2
            return temp[a]

    # Better without using O(m + n) space
    # TC = O(m + n)
    def findMedianSortedArrays(self, nums1, nums2):
        n = len(nums1) + len(nums2)
        i = 0
        j = 0
        k = 0
        idx1 = n // 2 - 1
        element1 = -1
        idx2 = n // 2
        element2 = -1

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                if k == idx1:
                    element1 = nums1[i]
                if k == idx2:
                    element2 = nums1[i]
                i += 1
            else:
                if k == idx1:
                    element1 = nums2[j]
                if k == idx2:
                    element2 = nums2[j]
                j += 1
            k += 1

        while i < len(nums1):
            if k == idx1:
                element1 = nums1[i]
            if k == idx2:
                element2 = nums1[i]
            i += 1
            k += 1

        while j < len(nums2):
            if k == idx1:
                element1 = nums2[j]
            if k == idx2:
                element2 = nums2[j]
            j += 1
            k += 1

        if n % 2 == 0:
            return (element1 + element2) / 2
        else:
            return element2

    # TC = O(log(min(nums1, nums2)))
    def findMedianSortedArrays(self, nums1, nums2):
        # Perform binary search on the small array
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums2)
        # small array length
        m = len(nums1)
        # large array length
        n = len(nums2)
        # small array lower bound
        l = 0
        # small array upper bound
        r = m
        while l <= r:
            Px = l + (r - l) // 2
            Py = (m + n + 1) // 2 - Px
            # left portion of the array
            # Px - 1 and Py - 1 because the index starts from 0 and if we want to get the last element we do length - 1
            l1 = float("-inf") if (Px == 0) else nums1[Px - 1]
            l2 = float("-inf") if (Py == 0) else nums2[Py - 1]
            # right portion of the array
            # Since index starts from 0 and from right side if we are looking for the first element then it will be equal to Px and Py
            r1 = float("inf") if (Px == m) else nums1[Px]
            r2 = float("inf") if (Py == n) else nums2[Py]

            if l1 <= r2 and l2 <= r1:
                if (m + n) % 2 == 0:
                    return (float(max(l1, l2)) + float(min(r1, r2))) / 2.0
                else:
                    return max(l1, l2)
            elif l1 > r2:
                r = Px - 1
            else:
                l = Px + 1
        return -1


answer = Solution()
nums1 = [2, 4, 9]
nums2 = [8, 12, 19]
print(answer.findMedianSortedArrays(nums1, nums2))
