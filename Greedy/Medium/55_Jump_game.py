class Solution:
    # TC = O(n)
    # SC = O(1)
    # If the array contains "0". You will never be able to reach the last index
    def canJump(self, nums):
        # maxJump - This keeps track of the farthest index you can reach so far.
        maxJump = 0
        for i in range(len(nums)):
            # At each index i, you're checking:
            # "Can I even reach this index from previous jumps?"
            # If i > maxJump, it means you’re stuck —
            # you can't reach this position, so it's impossible to continue,
            if i > maxJump:
                return False
            maxJump = max(nums[i] + i, maxJump)
            # to return early:
            # if maxJump == len(nums) - 1:
            #     return True
        return True

    # Brute force
    # TC = O(n ^ n)
    # Intution
    # "From this position, I can jump to several others.
    # Let's try all of them one by one and see if I can reach the end."
    def canJumpRecursiveBrute(self, nums):
        def canReach(self, index):
            if index == len(nums) - 1:
                return True
            farthestJump = min(nums[index] + index, len(nums) - 1)
            for nexPos in range(index + 1, farthestJump + 1):
                if canReach(nexPos):
                    return True
            return False

        return canReach(0)

    # NOTE:
    # index + nums[index] gives the farthestJump or maxJump
    # why min ?
    # Because index + nums[index] might go beyond the end of the array,
    # and if you try to access such indices, you'll get an IndexError

    # why min matters?
    """
    nums = [100, 1, 1, 1]
    position = 0
    → nums[0] = 100
    → position + nums[position] = 0 + 100 = 100
     But `len(nums) - 1 = 3` → index 100 doesn’t exist
    """


answer = Solution()
nums = [2, 3, 1, 1, 4]
print(answer.canJump(nums))
