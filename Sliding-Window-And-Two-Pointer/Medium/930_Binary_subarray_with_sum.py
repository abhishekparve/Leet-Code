class Solution:
    def numSubarraysWithSumBrute(self, nums, goal):
        subarray_count = 0
        for i in range(len(nums)):
            currSum = 0
            for j in range(i, len(nums)):
                currSum += nums[j]
                if currSum == goal:
                    subarray_count += 1
        return subarray_count

    def numSubarraysWithSumBetter(self, nums, goal):
        array_map = {0: 1}
        currSum = 0
        count = 0
        for i in range(len(nums)):
            currSum += nums[i]
            remaining_sum = currSum - goal
            count += array_map.get(remaining_sum, 0)
            array_map[currSum] = 1 + array_map.get(currSum, 0)
        return count

    # In numSubarraysWithSum:
    # 1. The sum is already equal to goal.
    # 2.You want to know how many prefixes (left shifts) you can chop off,
    #  where you're removing leading zeros, without changing the sum.
    # 3.count_zeros tracks how many such removable zeros there are.

    # Total valid subarrays ending at r: 1 (the full window) + count_zeros.
    # count_zeros tracks how many subarrays starting with leading zeros
    # are valid extensions of the current window ending at r and having sum == goal.

    # When r = 4, we have this subarray [0, 0, 1, 0, 1].
    # Possible valid subarrays that sum to 2:
    # [1, 0, 1]
    # [0, 1, 0, 1]
    # [0, 0, 1, 0, 1]

    # These all end at index 4 but start from different positions depending on how many leading zeros you skip.
    # So if count_zeros = 2, that means:
    # 1. One subarray with no zeros dropped
    # 2. One with one zero dropped
    # 3. One with both zeros dropped

    # This gives count_zeros + 1 valid subarrays.
    # TC = (2n)
    def numSubarraysWithSumOptimal(self, nums, goal):
        l = 0
        r = 0
        window_size = 0
        subarray_count = 0
        count_zeros = 0
        while r < len(nums):
            window_size += nums[r]
            while l < r and (nums[l] == 0 and window_size > goal):
                if nums[l] == 0:
                    count_zeros += 1
                else:
                    count_zeros = 0
                window_size -= nums[l]
                l += 1

            if window_size == goal:
                subarray_count += 1 + count_zeros
            r += 1
        return subarray_count

    # Striver's solution:
    # Exactly(goal) = AtMost(goal) - AtMost(goal - 1)
    # In a binary array, the sum of elements = number of 1s in the subarray. So:
    # AtMost(2) gives you all subarrays whose sum is 0, 1, or 2
    # AtMost(1) gives you all subarrays whose sum is 0 or 1
    # So if you subtract:
    # AtMost(2) - AtMost(1)

    # You’re removing all the subarrays with sum 0 or 1, and keeping only those with sum exactly 2.
    # AtMost(2) gives you all subarrays whose sum is 0, 1, or 2

    # TC  = 2 * O(2n)
    # multiply by two because we are calling the atMostGoal method twice
    def numSubarraysWithSum(self, nums, goal):
        def atMostGoal(goal):
            if goal < 0:
                return 0
            l = 0
            r = 0
            currSum = 0
            count = 0
            while r < len(nums):
                currSum += nums[r]
                while currSum > goal:
                    currSum -= nums[l]
                    l += 1
                if currSum <= goal:
                    count += r - l + 1
                r += 1
            return count

        return atMostGoal(goal) - atMostGoal(goal - 1)


answer = Solution()
nums = [1, 0, 1, 0, 1]
goal = 2
print(answer.numSubarraysWithSumBrute(nums, goal))
print(answer.numsSubarraysWithSumBetter(nums, goal))
# code story with mike solution
print(answer.numsSubarraysWithSumOptimal(nums, goal))
# Striver's solution
print(answer.numSubarraysWithSum(nums, goal))
