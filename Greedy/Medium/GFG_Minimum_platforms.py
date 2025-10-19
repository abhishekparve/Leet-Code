class Solution:
    # Here we are trying to check wheather the arrival and departure
    # time of each trains overlaps with the timings of the other train
    # If it overlaps we increment the platfrom_needed count by one
    # TC = O(n ^ 2)
    # SC = O(1)
    def findPlatform(self, arr, dep):
        n = len(arr)
        max_platform = 0
        for i in range(n):
            platform_needed = 1
            for j in range(n):
                if i != j and arr[i] <= dep[j] and arr[j] <= dep[i]:
                    platform_needed += 1
                max_platform = max(max_platform, platform_needed)
        return max_platform

    # We don't need to match specific trains.
    # Instead, we only care how many trains are at the station at the same time.
    # That tells us the number of platforms needed at that time.
    # So we sort both the arrival and departure time

    # i points to the next train to arrive
    # j points to the next train to depart

    """
    We scan time forward. At each moment, we decide:

    If the next train arrives before the current one departs (arr[i] <= dep[j]):

    We need another platform
    So, platform_needed += 1, and move i forward.

    Else (train departs before the next arrives):

    One platform gets freed → platform_needed -= 1
    Move j forward.
    """

    # TC = O(2(n + nlogn)
    # 2n  because we are iterating both the arrays
    # 2(n logn) for sorting both the arrays
    def findPlatformTwoPointer(self, arr, dep):
        n = len(arr)
        arr.sort()
        dep.sort()
        i = 1
        j = 0
        platform_needed = 1
        max_platform = 1
        while i < n and j < n:
            if arr[i] <= dep[j]:
                platform_needed += 1
                i += 1
            else:
                platform_needed -= 1
                j += 1
            # We track the maximum platforms needed at each moment
            max_platform = max(platform_needed, max_platform)
        return max_platform


"""
Why do we start with i = 1 ?

This is intentional

i points to the next train to arrive.
j points to the next train to depart.

At the very beginning:
The first train has arrived (arr[0]).
So we start with one platform already needed.
From there,
If the next arriving train (arr[i]) arrives before or at the same time as the earliest departure (dep[j]),
we need a new platform. Otherwise, a platform is freed up (train j departs), and we can reuse it.

if i = 0 and j = 0
You’d compare the first train's arrival with the first train’s departure — that's the same train,
which doesn't make sense. A train shouldn't be compared with itself.
"""

answer = Solution()
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
