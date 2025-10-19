# https://www.naukri.com/code360/problems/allocate-books_1090540?utm_source=striver&utm_medium=website&utm_campaign=codestudio_a_zcourse


class Solution:
    # TC = O(sum - max + 1)*O(n)
    def findMinPagesBrute(self, arr, m):
        start = max(arr)  # O(n)
        end = sum(arr)  # O(n)
        for i in range(start, end + 1):  # O(sum - max + 1)
            no_of_students = self.allocatePages(arr, i)
            if no_of_students == m:
                return i
        return start

    # TC = O(log(sum - max + 1)*O(n))
    def findMinPagesOptimal(self, arr, m):
        l = max(arr)
        r = sum(arr)
        while l <= r:
            mid = l + (r - l) // 2
            no_of_students = self.allocatePages(arr, mid)
            if no_of_students > m:
                l = mid + 1
            else:
                r = mid - 1
        return l

    def allocatePages(self, arr, pages):
        student = 1
        countPages = 0
        for i in range(len(arr)):
            if countPages + arr[i] <= pages:
                countPages += arr[i]
            else:
                student += 1
                countPages = arr[i]
        return student


answer = Solution()
arr = [25, 46, 28, 49, 24]
m = 4
print(answer.findMinPagesBrute(arr, m))
print(answer.findMinPagesOptimal(arr, m))
