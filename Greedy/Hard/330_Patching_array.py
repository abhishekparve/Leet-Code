class Solution:
    # Same as : LC-2952. Minimum Number of Coins to be Added
    # TC = O(log n + m), where m is len(nums)
    def minPatches(self, nums, n):
        patches = 0
        maxReach = 0
        index = 0
        while maxReach < n:
            if index < len(nums) and nums[index] <= maxReach + 1:
                maxReach += nums[index]
                index += 1
            else:
                patches += 1
                maxReach += maxReach + 1
        return patches


answer = Solution()
nums = [1, 5, 10]
n = 20
print(answer.minPatches(nums, n))

"""Two Cases Inside the Loop:
Case 1: nums[index] <= maxReach + 1
We can use the current number in nums to extend our reach.

We increment index, so we make at most len(nums) such steps.

Total time spent here: O(len(nums))

Case 2: nums[index] > maxReach + 1 or no more numbers
We patch a number (add maxReach + 1), and increase maxReach by that value.

After patching:

new maxReach = maxReach + (maxReach+1) =2 ⋅ maxReach+1
new maxReach = maxReach + (maxReach+1) =2 ⋅ maxReach+1
This grows exponentially, so the number of such patch steps is bounded by O(log n)."""
