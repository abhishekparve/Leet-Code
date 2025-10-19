# https://www.geeksforgeeks.org/dsa/connect-n-ropes-minimum-cost/
import heapq


class Solution:
    # Intution : connecting the first two smallest ropes will lead to a minimum cost
    #            so
    #            1. we sort the array first
    #            2. then pop the the two elements from the start
    #            3. calculate the sum and add it to the total
    #            4. again append the sum of the first two elements back into the nums list
    # TC = O(n * nlogn)
    def minCost(self, nums):
        total = 0
        while len(nums) > 1:
            nums.sort()
            first = nums.pop(0)
            second = nums.pop(0)
            cost = first + second
            total += cost
            nums.append(cost)
        return total

    # TC = O(nlog(n))
    def minCostHeap(self, nums):
        # Since we want to find the min cost
        # we need to pop min elements from the heap in O(log(n))
        # So the heap which has the minimum elements at the top is our min heap
        min_heap = []
        # You can also write as
        # heapq.heapify(nums)
        for i in range(len(nums)):
            heapq.heappush(min_heap, nums[i])

        total = 0
        while len(min_heap) > 1:
            first = heapq.heappop(min_heap)
            second = heapq.heappop(min_heap)
            cost = first + second
            total += cost
            heapq.heappush(min_heap, cost)
        return total


answer = Solution()
nums = [4, 3, 2, 6]
nums2 = [4, 3, 2, 6]
print(answer.minCost(nums))
print(answer.minCostHeap(nums2))
