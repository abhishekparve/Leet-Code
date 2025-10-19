# https://www.geeksforgeeks.org/problems/row-with-max-1s0023/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=row-with-max-1s


class Solution:
    def rowsWithMax1sBrute(self, arr):
        max_ones = 0
        index = -1
        for i in range(len(arr)):
            count_ones = 0
            for j in range(len(arr[i])):
                if arr[i][j] == 1:
                    count_ones += 1
            if count_ones > max_ones:
                max_ones = count_ones
                inde+x = i
        return index

    def lowerBound(self, arr, target):
        l = 0
        r = len(arr) - 1
        res = len(arr)
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] >= target:
                res = mid
                r = mid - 1
            elif arr[mid] < target:
                l = mid + 1
        return res

    def rowsWithMax1sOptimal(self, arr):
        max_ones = 0
        index = -1
        m = len(arr)
        for i in range(len(arr)):
            count_ones = m - self.lowerBound(arr[i], 1)
            if count_ones > max_ones:
                max_ones = count_ones
                index = i
        return index


answer = Solution()
arr = [[0, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]]
# result = answer.rowsWithMax1sBrute(arr)
result = answer.rowsWithMax1sOptimal(arr)
print(result)
