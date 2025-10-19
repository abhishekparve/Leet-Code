class Solution:
    # TC = O(n + n logn + n)
    def fractionalknapsack(self, val, wt, capacity):
        i = 0
        j = 0
        # arr = list(zip(val, wt))
        # OR you can go with below technique
        arr = []
        while i < len(val) and j < len(val):
            arr.append((val[i], wt[j]))
            i += 1
            j += 1
        # x reperesents the tuple (val, wt) --> [0, 1]
        # x[0] = val and x[1] = wt
        arr.sort(key=lambda x: x[0] / x[1], reverse=True)
        total = 0.0
        for value, weight in arr:
            if weight <= capacity:
                total += value
                capacity -= weight
            else:
                total += (value / weight) * capacity
                break
                # we are breakinf bcz we have calculated the partial weight value and
                # we have exhausted our capacity
        return total


answer = Solution()
val = [60, 100, 120]
wt = [10, 20, 30]
capacity = 50
print(answer.fractionalknapsack(val, wt, capacity))

# In the this problem, if we start taking the weights
# who's values are greater we might find maximum the total value
# But this cannot always end up giving the maximum total value
# consider below example
# val = [100, 60, 100, 200]
# wt  = [20, 10,  50,  90]
# cap = 90
# if we take the value 200, since it has the max value
# we are also exhausting the capacity because the corresponding weight for the value is also 90
# and that is equal to the capacity. As a result we will not be able to pick any more weights
# But if we take the other values like 100, 60, 100 and partial of (200 ~ 22.22 [(200/90)*10])
# we get total value as 282.22 which is greater than 200
# So what to pick?
# we can pick weights based on value per weight
# if wt = 20, val = 100
# value per weight = 100/20 => 5
# So here we can pick those weights whose value/weight is greater
# for above example value/weight = [5, 6, 2, 4]
# and then we can sort in descending to only pick max values
# NOTE
# 30 kg wt -------> 120 value
# 1kg wt  --------> 120/30
# So for, 20 kg (remaining capacity)
# 20 kg wt --------> (120/30) * 20
