class Solution:
    def minJumpBrute(self, nums):
        def canReach(index):
            if index == len(nums) - 1:
                return 0
            farthestJump = min(nums[index] + index, len(nums) - 1)
            min_jumps = float("inf")
            for nextPos in range(index + 1, farthestJump + 1):
                jump = canReach(nextPos)
                if jump != float("inf"):
                    min_jumps = min(min_jumps, jump + 1)
            return min_jumps

        return canReach(0)

    """
    # Intution

    1. Start at index 0, with a range [l, r] initialized to [0, 0]
    — meaning you're currently at position 0 and you haven't jumped yet.

    2. In each iteration of the while loop:
    -- You're processing the current "level" of reachable indices (from l to r).
    -- You want to know: what's the farthest you can reach from any index in this range?
    -- This becomes your next range — and you increment your jump count to get there.

    3. Update l and r to represent the new range:
    -- l = r + 1 (start of next level)
    -- r = farthestJump (end of next level)

    4. Repeat until r covers the last index.
    """

    # TC = O(n)
    # SC = O(1)
    def minJump(self, nums):
        l = 0
        r = 0
        jump = 0
        while r < len(nums) - 1:
            farthestJump = 0
            for i in range(l, r + 1):
                farthestJump = max(nums[i] + i, farthestJump)
            l = r + 1
            r = farthestJump
            jump += 1
        return jump


answer = Solution()
nums = [2, 3, 1, 1, 4]
print(answer.minJumpBrute(nums))
