# https://www.naukri.com/code360/problems/painter-s-partition-problem_1089557?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf


class Solution:
    # TC = O(sum - max + 1)*O(n)
    def findLargestMinDistanceBrute(self, boards, k):
        start = max(boards)
        end = sum(boards)
        for i in range(start, end + 1):
            min_splits = self.computeSplit(boards, i)
            if min_splits == k:
                return i
        return start

    # TC = O(log(sum - max + 1)*O(n))
    def findLargestMinDistanceOptimal(self, boards, k):
        l = max(boards)
        r = sum(boards)
        while l <= r:
            mid = l + (r - l) // 2
            min_splits = self.computeSplit(boards, mid)
            if min_splits > k:
                l = mid + 1
            else:
                r = mid - 1
        return l

    def computeSplit(self, boards, maxSum):
        k = 1
        sum_of_subarray = 0
        for i in range(len(boards)):
            if sum_of_subarray + boards[i] <= maxSum:
                sum_of_subarray += boards[i]
            else:
                k += 1
                sum_of_subarray = boards[i]
        return k


answer = Solution()
boards = [10, 20, 30, 40]
k = 2
print(answer.findLargestMinDistanceBrute(boards, k))
print(answer.findLargestMinDistanceOptimal(boards, k))
