class Solution:
    # TC = O(n^3)
    # SC = O(n)
    def longestOnesBrute(self, nums, k):
        max_length = 0
        for i in range(len(nums)):
            zeros = 0
            for j in range(i, len(nums)):
                if nums[j] == 0:
                    zeros += 1
                if zeros <= k:
                    max_length = max(max_length, j - i + 1)
                else:
                    break
        return max_length

    # TC = O(2n)
    # SC = O(n)
    def longestOnesBetter(self, nums, k):
        l = 0
        r = 0
        max_length = 0
        zeros = 0
        while r < len(nums):
            if nums[r] == 0:
                zeros += 1
            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            if zeros <= k:
                max_length = max(max_length, r - l + 1)
            r += 1
        return max_length

    # TC = O(n)
    # SC = O(n)
    def longestOnesOptimal(self, nums, k):
        l = 0
        r = 0
        max_length = 0
        zeros = 0
        while r < len(nums):
            if nums[r] == 0:
                zeros += 1
            if zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            if zeros <= k:
                max_length = max(max_length, r - l + 1)
            r += 1
        return max_length


answer = Solution()
nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
print(answer.longestOnesOptimal(nums, k))
print(answer.longestOnesBetter(nums, k))
print(answer.longestOnesBrute(nums, k))
