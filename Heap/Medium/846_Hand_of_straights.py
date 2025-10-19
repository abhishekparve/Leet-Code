import heapq


class Solution:
    # TC = O(n * log(n))
    def isNStraightHand(self, hand, groupSize):
        # If len(hand) is not divsible by groupSize
        # then return False
        if len(hand) % groupSize:
            return False

        count = {}
        # Sorting the cound for each hand[i] in count map
        for i in range(len(hand)):
            count[hand[i]] = count.get(hand[i], 0) + 1

        minHeap = []
        # Storing all the count keys in minHeap list
        # Another way of doing this in python is minHeap = lists(count.keys())
        for key in count.keys():
            minHeap.append(key)
        # converting the list into minHeap
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]
            # curr, curr + 1, curr + 2...so on
            # if n = 2, first = 0
            # range = (0 -> 0 + 2) -- (0, 2) which means from 0 to 1 and excluding 2
            # range = (1 -> 1 + 2 ) --(1, 3)
            # range = (2 -> 2 + 2) --(2, 4)
            # curr ~ first
            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True


answer = Solution()
hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
groupSize = 3
print(answer.isNStraightHand(hand, groupSize))
