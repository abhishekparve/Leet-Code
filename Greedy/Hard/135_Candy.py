class Solution:
    # TC = O(3n)
    # SC = O(2n)
    def candyBrute(self, ratings):
        n = len(ratings)
        # Assigning atleast one candy
        left = [1] * n
        right = [1] * n

        # left to right traversal while comparing the ratings of the left neighbour
        for i in range(1, n):
            if i - 1 >= 0 and ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
            # else loop not needed as we have already initialized left array with 1
            else:
                left[i] = 1

        # right to left traversal while comparing the ratings of the right neighbour
        for i in range(n - 2, -1, -1):
            if i + 1 < n and ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1
            # else loop not needed as we have already initialized right array with 1
            else:
                right[i] = 1

        total = 0
        for i in range(n):
            total += max(left[i], right[i])
        return total

    # No need to maintain the right array for the right neighbours
    """
    Why max(candies[i], right)?

    We already made sure candies[i] satisfies the left side.
    Now, right is the minimum needed to satisfy the right side.

    So, to satisfy both, we take: max(candies[i], right)

    right += 1 is needed when the current child is greater than the right neighbor, 
                so they get at least 1 more candy than that neighbor.

    max(candies[i], right) ensures we satisfy both left and right neighbor conditions.

    Why do we start with right = 1?

    right represents the minimum candies needed to satisfy the condition that a child with
    a higher rating than their right neighbor should get more candies than that neighbor.

    So, for the last child (i = n-1), who has no right neighbor:
    We can safely give them 1 candy, so right = 1 is the correct starting value.
    """

    def candyBetter(self, ratings):
        n = len(ratings)
        candies = [1] * n

        for i in range(1, n):
            if i - 1 >= 0 and ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        total = 0
        right = 1
        # we use a temporary variable right to track the minimum candies
        # that would satisfy the right neighbor rule.
        for j in range(n - 1, -1, -1):
            if j + 1 < n and ratings[j] > ratings[j + 1]:
                right += 1
            else:
                right = 1
            total += max(candies[j], right)

        return total

    # Slope concept

    """
    This solution treats the ratings as a sequence of slopes:

    Increasing slopes (children who need more candies than the previous one),

    Decreasing slopes (children who need fewer candies than the previous one),

    and flat sections (equal ratings — no need to increase or decrease candies).

    Instead of assigning candies to each child directly, it counts how many additional candies are 
    needed by summing triangular numbers for both increasing and decreasing slopes.

    ----------------------------------------------------------------------------------------

    Each child must get at least 1 candy → So we start with candies = n (1 per child).

    For every increasing or decreasing sequence:

    You add a "triangle number" for the extra candies.

    E.g., for an increasing slope of length 3 (ratings like [1, 2, 3, 4]), you'd add 1 + 2 + 3 = 6 extra candies.

    At the peak point (where increasing switches to decreasing), the highest point is counted twice,
    once in the up and once in the down slope, so we subtract min(peak, dip) to fix the overcount.
    """

    # TC = O(n)
    # SC = O(1)
    def candyOptimal(self, ratings):
        n = len(ratings)
        i = 1
        # Each child must get at least 1 candy → So we start with candies = n (1 per child).
        candies = n
        while i < n:
            # If the ratings are same we increment i by 1
            if ratings[i - 1] == ratings[i]:
                i += 1
                continue

            # Once every mountain is completed i.e after the end of each increaing and decreasing curve
            # we initialize peak = 0 and dip = 0 for th new mountain
            peak = 0
            while ratings[i] > ratings[i - 1]:
                peak += 1
                candies += peak
                i += 1
                # If there is only increasing curve till the i reaches the n
                # then we straight up return the total candies
                if i == n:
                    return candies

            dip = 0
            while i < n and ratings[i] < ratings[i - 1]:
                dip += 1
                candies += dip
                i += 1
            # After the end of every mountain, we fix the overcount
            # At the peak point (where increasing switches to decreasing), the highest point is counted twice,
            # once in the up and once in the down slope, so we subtract min(peak, dip) to fix the overcount.
            candies -= min(peak, dip)
        return candies


answer = Solution()
ratings = [1, 2, 2]
print(answer.candyBrute(ratings))
print(answer.candyBetter(ratings))
print(answer.candyOptimal(ratings))
