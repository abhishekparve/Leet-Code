import heapq
from collections import deque


class Solution:
    # TC = O(n logn)
    def leastIntervalHeap(self, tasks, n):
        map = {}
        # Creating a map with the count of each character
        # O(26)
        for i in range(len(tasks)):
            map[tasks[i]] = map.get(tasks[i], 0) + 1

        maxHeap = []
        # Iterating over the map values and
        # Adding negative values in maxHeap list
        # As python has bu default min-heap, to establish max-heap
        # property we push negative values in heap
        # O(26)
        for val in map.values():
            maxHeap.append(-val)
        # Converting the maxHeap array to Heap
        # O(nlogn)
        heapq.heapify(maxHeap)

        # creating queue
        # In queue we will push the [remaining count, next execution time]
        # next execition time = current time + n (Interval)
        queue = deque()
        time = 0
        # O(n) + O(n logn)
        while maxHeap or queue:
            time += 1
            if maxHeap:
                # plus one beacuse we are decrementing it
                # we initailly added negative values in heap
                # to decrement it we have to add positive one
                count = 1 + heapq.heappop(maxHeap)
                # If count is not zero then we append [count, ET] in queue
                if count:
                    queue.append([count, time + n])

            if queue and queue[0][1] == time:
                # queue[0][1] is the second value which is the executime time
                # queue.popleft()[0] will return the count
                heapq.heappush(maxHeap, queue.popleft()[0])
        return time

    # TC = O(n logn)
    def leastIntervalGreedyUsingArray(self, tasks, n):
        if n == 0:
            return len(tasks)

        charArray = [0] * 26
        for task in tasks:
            charArray[ord(task) - ord("A")] += 1

        charArray.sort()
        maxFreq = charArray[25]
        # gaddhe
        emptySpaces = maxFreq - 1
        # har gaddhe mai n slots chode honge
        # so gaddhe * n
        idelSlots = emptySpaces * n

        for i in range(24, -1, -1):
            idelSlots -= min(charArray[i], emptySpaces)

        if idelSlots > 0:
            return len(tasks) + idelSlots
        else:
            return len(tasks)

    #  TC = O(n logn)
    # SC = O(2n)
    def lastIntervalGreedyUsingMap(self, tasks, n):
        map = {}
        for i in range(len(tasks)):
            map[tasks[i]] = map.get(tasks[i], 0) + 1

        res = []
        for val in map.values():
            res.append(val)

        res.sort()

        maxFreq = res[len(res) - 1]
        emptySpaces = maxFreq - 1
        idleSpaces = emptySpaces * n
        for i in range(len(res) - 2, -1, -1):
            idleSpaces -= min(res[i], emptySpaces)

        if idleSpaces > 0:
            return len(tasks) + idleSpaces
        else:
            return len(tasks)


answer = Solution()
tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
print(answer.leastIntervalHeap(tasks, n))
print(answer.leastIntervalGreedyUsingArray(tasks, n))
print(answer.lastIntervalGreedyUsingMap(tasks, n))
