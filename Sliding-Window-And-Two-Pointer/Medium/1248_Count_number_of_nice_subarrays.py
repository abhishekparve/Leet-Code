class Solution:
    # TC = O(n)
    # SC = O(n)
    def numberOfSubarrays(self, nums, k):
        arrayMap = {0: 1}
        result = 0
        curr_count = 0
        for i in range(len(nums)):
            curr_count += nums[i] % 2
            remaining_count = curr_count - k
            result += arrayMap.get(remaining_count, 0)
            arrayMap[curr_count] = arrayMap.get(curr_count, 0) + 1
        return result

    # In numberOfSubarrays (Exactly k odds):
    # 1. The current window has exactly k odd numbers.
    # 2. You try to move l forward over even numbers to find shorter valid subarrays as even numbers
    #    do not contribute to the ideal subarray
    # 3. Each valid left shift increases prev_count, until an odd is removed.
    # 4. prev_count then gets reused for upcoming even elements at r.

    # TC = O(2n)
    # SC = O(1)
    def numberOfSubarraysCodeStory(self, nums, k):
        prev_count = 0
        odd_count = 0
        l = 0
        r = 0
        count = 0
        while r < len(nums):
            # when you encounter the odd element reset the prev_count
            if nums[r] % 2 == 1:
                odd_count += 1
                prev_count = 0
            # when odd_count == k
            # keep incrementing the prev_count and l pointer
            # In a way you are skipping the even elements as they do not
            # contribute to your subarray criteria.
            # But when you encounter an odd element you decrement the odd_count
            while odd_count == k:
                prev_count += 1
                if nums[l] % 2 == 1:
                    odd_count -= 1
                l += 1

            count += prev_count
            r += 1
        return count

    # Same solution as LC - 930. Just performing modulo operation
    def numberOfSubarraysCodeStriver(self, nums, k):
        def atMost(target):
            if target < 0:
                return 0
            l = 0
            r = 0
            currSum = 0
            count = 0
            while r < len(nums):
                if nums[r] % 2 == 1:
                    currSum += nums[r] % 2

                while currSum > target:
                    currSum -= nums[l] % 2
                    l += 1
                if currSum <= target:
                    count += r - l + 1
                r += 1
            return count

        return atMost(k) - atMost(k - 1)


answer = Solution()
nums = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
k = 2
print(answer.numberOfSubarrays(nums, k))
print(answer.numberOfSubarraysCodeStory(nums, k))
print(answer.numberOfSubarraysCodeStriver(nums, k))
