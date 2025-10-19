# Similar to median of sorted array
class Solution:
    def kthElement(self, arr1, arr2, k):
        if len(arr1) > len(arr2):
            self.kthElement(arr2, arr1, k)
        # len of arr1
        m = len(arr1)
        # len of arr2
        n = len(arr2)
        # Since we are considering the smaller array and we are looking for the kth element
        # then the upper bound will be at min value of k or all the elements from arr1(m)
        # the lower bound will be either we will not select any value i.e., 0 or at max (k -n) elements
        l = max(0, k - n)
        r = min(k, m)

        while l <= r:
            Px = l + (r - l) // 2
            Py = k - Px
            l1 = float("-inf") if (Px == 0) else arr1[Px - 1]
            l2 = float("-inf") if (Py == 0) else arr1[Py - 1]
            r1 = float("inf") if (Px == m) else arr1[Px]
            r2 = float("inf") if (Px == n) else arr1[Py]
            if l1 <= r2 and l2 <= r1:
                return max(l1, l2)
            elif l1 > r2:
                r = Px - 1
            else:
                l = Px + 1
        return 0


answer = Solution()
k = 5
arr1 = [2, 3, 6, 7, 9]
arr2 = [1, 4, 8, 10]
print(answer.kthElement(arr1, arr2, k))


# Let's take an example, m = 3, n = 10, k = 12
# If we keep low = 0, and high = 3
# then mid1 = 1;
# low = 0 means we don't pick any element from the first array, and now the remaining elements need to be picked from the second array.
# mid2 = (k - mid1) = 12 - 1 = 11 ???? but there are only 10 elements in the second array
# Hence we can't start our search when we pick no elements from the first array.
# So our low must be max(k - n, 0) [no of elements  at least need to pick for 1st array]
# Similarly, for high, we have to reduce the search space such that it can handle low K values.

# Note: this issue doesn't occur in the median problem because we guaranteed to split the search space in half every time.
