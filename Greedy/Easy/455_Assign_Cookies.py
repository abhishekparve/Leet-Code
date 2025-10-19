class Solution:
    # TC = O(m logm) + O(n logn) + O(m + n)
    def findContentChildren(self, g, s):
        # length of children array
        m = len(g)
        # length of cookie size
        n = len(s)
        # Here te idea is to assign smaller size cookie to the child
        # that has the minimum capacity(greed). So that we can save the
        # large size cookie for the children that has the maximum greed.
        # That's why we sort
        # If we don't sort, we might end up exhausting the max size cookies for the
        # children that has smaller greed and then we won't be able to satisfy children
        # with max greed factor

        # sorting both the arrays
        g.sort()
        m.sort()
        i = 0
        j = 0
        # two pointers
        while i < m and j < n:
            if g[i] <= s[j]:
                i += 1
            j += 1
        # we will keep on incrementing the j to find the cookie size
        # that satisfies the child's greed.
        # Note :We will not increment the i
        # until we greed factor for that paticular child is satisfied

        # "i" will point to the number of children that are satisfied.
        return i
