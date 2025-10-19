# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/


class Solution:
    # TC = O(k ^ 2)
    def maxScoreBrute(self, cardPoints, k):
        n = len(cardPoints)
        max_sum = 0
        # i = number of cards taken from the front
        # k - i = number of cards taken from the back
        # its basic arithmetic if you have to pick k elements
        # and if you pick i element at front then the remaining elements that
        # you have to pick will be (k - i)
        for i in range(k + 1):
            # Starting from zero pick every thing till "i" but exclude i index
            front = sum(cardPoints[:i])
            # So what is n - (k - i)?
            # It gives you the starting index of the last k - i cards in the array.
            # Let’s break it down further:
            # 1. n is the total number of cards
            # 2. k - i is how many we want from the end
            # 3. n - (k - i) is the index where the last k - i cards start
            back = sum(cardPoints[n - (k - i) :])
            total = front + back
            max_sum = max(max_sum, total)
        return max_sum

    # Why the for loop is in the range k + 1 and not k?
    #  i_index        front pick     back pick (k - i)
    #     0              0               3
    #     1              1               2
    #     2              2               1
    #     3              3               0

    # If we did range(k), we would stop at k - 1 which is "2" index
    # and we would have missed all the cases where "k" cards are picked
    # from the front.
    # Intitution :
    # We are trying to split k picks between front and back
    # 1. from 0 front + k back
    # 2. to k front + 0 back
    # and that is exactly k + 1 combinations

    # TC = O(2k)
    def maxScoreOptimal(self, cardPoints, k):
        l_sum = 0
        r_sum = 0
        n = len(cardPoints)
        # calculating the sum of the first k element
        # from the left (O(k))
        for i in range(k):
            l_sum += cardPoints[i]
        # Initially max_sum will be equla to l_sum
        # because that is the max we have so far
        max_sum = l_sum
        # To pick from back, we need to get the last index
        # which is n - 1
        r_index = n - 1
        # if we have picked k size array then the last index will be k - 1
        # and from there we keep moving towards left k - 2, k - 3,..so on.
        # while decrementing from the front we also keep on adding the
        # same number of remove elements from the back i.e, n - 1, n- 2, n- 3
        # and so on.. (O(k))
        for i in range(k - 1, -1, -1):
            l_sum -= cardPoints[i]
            r_sum += cardPoints[r_index]
            max_sum = max(max_sum, l_sum + r_sum)
            r_index -= 1
        return max_sum


answer = Solution()
cardPoints = [1, 2, 3, 4, 5, 6, 1]
k = 3
print(answer.maxScoreBrute(cardPoints, k))
print(answer.maxScoreOptimal(cardPoints, k))
