# https://leetcode.com/problems/kth-missing-positive-number/description/


# TC = O(log(n))
class Solution:
    # Brute = TC = O(n)
    # You want to find the k-th missing positive number,
    # assuming you're counting from 1 upward.

    # Let’s say:
    # arr = [2, 3, 4, 7, 11]
    # k = 5
    # So at the beginning, you think the 5th missing number is 5,
    # if no actual values in arr interfered.

    # But the problem is: some numbers that you think are missing may actually exist in arr.

    # You go through the array, checking if arr[i] is less than or equal to k

    # If it is, it means:
    # “This number is not missing — I wrongly assumed it was.”

    # So, you compensate by increasing k:
    # "If I thought the 5th missing number was 5, but actually 3 is in the array (not missing),
    # then the 5th missing must be further ahead — say 6 or 7.”

    def findKthPositiveBrute1(self, arr, k):
        for i in range(len(arr)):
            if arr[i] <= k:
                k += 1
            else:
                break
        return k

    # Brute TC = O(n + k)
    def findKthPositiveBrute2(self, arr, k):
        num = 1
        i = 0
        while i < len(arr) and k > 0:
            if arr[i] == num:  # No number missing
                i += 1
            else:  # number is missing
                k -= 1  # we've found one missing number

            num += 1  # move to the next number

        # [1, 2, 3] and k = 2 and num = 4 at this point
        # So k will remain unchanged
        # No number missing we handle this edge case
        while k:
            k -= 1
            num += 1

        # We subtract 1 because num has been incremented after the last valid missing number was found.
        return num - 1

    def findKthPositive(self, arr, k):
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = l + (r - l) // 2
            no_of_missing_elem = arr[mid] - (mid + 1)
            if no_of_missing_elem < k:
                l = mid + 1
            else:
                r = mid - 1
        return l + k


answer = Solution()
arr = [2, 3, 4, 7, 11]
k = 5
print(answer.findKthPositive(arr, k))
