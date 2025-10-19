class Solution:
    # TC = O(n ^ 2)
    # SC = O(n)
    def findSubarrayBrute(self, nums, k):
        count = 0
        for i in range(len(nums)):
            numSet = set()
            for j in range(i, len(nums)):
                numSet.add(nums[j])
                if len(numSet) == k:
                    count += 1
                elif len(numSet) > k:
                    break
        return count

    # TC = O(2n)
    # SC = O(n)
    def findSubarrayApproach1(self, nums, k):
        def AtMost(k):
            l = 0
            r = 0
            count = 0
            nums_map = {}
            while r < len(nums):
                nums_map[nums[r]] = nums_map.get(nums[r], 0) + 1

                while len(nums_map) > k:
                    nums_map[nums[l]] -= 1
                    if nums_map[nums[l]] == 0:
                        del nums_map[nums[l]]
                    l += 1

                if len(nums_map) <= k:
                    # Number of subarrays till r
                    count += r - l + 1
                r += 1
            return count

        return AtMost(k) - AtMost(k - 1)

    # TC = O(3n)
    # SC = O(n)
    # CodeStory Solution
    def findSubarrayApproach2(self, nums, k):
        count = 0
        i = 0
        j = 0
        i_big = 0
        nums_map = {}
        while j < len(nums):
            nums_map[nums[j]] = nums_map.get(nums[j], 0) + 1

            # If the subarray is not valid then shrink the window
            while len(nums_map) > k:
                nums_map[nums[i]] -= 1
                if nums_map[nums[i]] == 0:
                    del nums_map[nums[i]]
                i += 1
                i_big = i

            # find the smallest valid subarray till j
            while nums_map[nums[i]] > 1:
                nums_map[nums[i]] -= 1
                i += 1

            if len(nums_map) == k:
                count += 1 + i - i_big
            j += 1
        return count


answer = Solution()
nums = [3, 1, 2, 2, 3]
k = 3
print(answer.findSubarrayBrute(nums, k))
print(answer.findSubarrayApproach1(nums, k))
print(answer.findSubarrayApproach2(nums, k))
