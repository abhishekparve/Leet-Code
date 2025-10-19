# https://leetcode.com/problems/sum-of-subarray-minimums/description/


class Solution:
    def sumOfSubarrayMinBrute(self, arr):
        total = 0
        res = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr) + 1):
                res.append(arr[i:j])
                total += min(arr[i:j])
        return total

    def getNSEL(self, arr):
        n = len(arr)
        res = [0] * n
        stack = []
        for i in range(n):
            if len(stack) == 0:
                res[i] = -1
            else:
                while stack and arr[i] < arr[stack[-1]]:
                    stack.pop()
                res[i] = -1 if len(stack) == 0 else stack[-1]
            stack.append(i)
        return res

    def getNSER(self, arr):
        n = len(arr)
        res = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            if len(stack) == 0:
                res[i] = n
            else:
                while stack and arr[i] <= arr[stack[-1]]:
                    stack.pop()
                res[i] = n if len(stack) == 0 else stack[-1]
            stack.append(i)
        return res

    # TC = O(3n) SC = O(2n)
    def sumOfSubarrayMin(self, arr):
        NSEL = self.getNSEL(arr)
        NSER = self.getNSER(arr)
        total = 0
        MOD = 10**9 + 7
        for i in range(len(arr)):
            leftSmallerElement = NSEL[i] - i
            rightSmallerElement = i - NSER[i]
            total += (leftSmallerElement * rightSmallerElement) * arr[i]
        return total * MOD


answer = Solution()
arr = [3, 1, 2, 4]
print(answer.sumOfSubarrayMinBrute(arr))
print(answer.sumOfSubarrayMin(arr))


# Take this:


# arr = [3, 1, 2, 4]
#           ↑
#          i = 1
# Left of 1:
# [3] → one element ≥ 1 ⇒ L = 1

# Right of 1:
# [2, 4] → two elements ≥ 1 ⇒ R = 2

# Now let’s count how many subarrays you can build that include 1 and have only those elements

# Possible left boundaries:

# Include 0 elements before 1 (just [1])

# Include 1 element before 1 (e.g., [3,1])

# → That’s L + 1 = 2 options

# Possible right boundaries:
# Include 0 elements after 1 (e.g., [1])

# Include 1 element after 1 (e.g., [1,2])

# Include 2 elements after 1 (e.g., [1,2,4])

# → That’s R + 1 = 3 options

# ✅ Combining Left and Right
# For each of the (L + 1) ways to go left,
# you can pair it with each of the (R + 1) ways to go right.

# So total subarrays including 1 and only elements ≥ 1:

# (𝐿+1)×(𝑅+1)
# (L+1)×(R+1)
# This covers:

# [1], [1,2], [1,2,4]

# [3,1], [3,1,2], [3,1,2,4]

# → 6 subarrays total, as expected.

# General Rule:
# Whenever you fix a position (e.g., where the minimum value occurs),
# you can count subarrays by extending left and right as far as possible,
# and the total number of combinations is simply:

# ways to choose left boundary × ways to choose right boundary

# which is:

# (𝐿+1)×(𝑅+1)
