import heapq


class Solution:
    # TC = O(n ^ 2)
    # SC = O(2n) for returning the result and set
    def arrayRankTransformBrute(self, arr):
        result = [0] * len(arr)
        for i in range(len(arr)):
            arraySet = set()
            for j in range(len(arr)):
                # adding all the elements that are less than arr[i] in set
                if arr[j] < arr[i]:
                    arraySet.add(arr[j])
            # getting the length of the arraySet + 1 will give us the rank of
            # the elem at index i
            result[i] = len(arraySet) + 1
        return result

    # creating a set => O(n)
    # Sorting the set => O(nlogn)
    # Iterating over the set and filling the map ==> O(n) approx
    # Iterating over the array again to populate the rank based on the element map ranking => O(n)
    # TC = O(n) + O(nlogn) + O(n) + O(n)
    # SC = O(n) (map) + O(n) (arraySet) + O(n) result ==> O(3n)

    def arrayRankTransform(self, arr):
        n = len(arr)
        result = [0] * n
        arraySet = sorted(set(arr))
        map = {}
        rank = 0
        for i in range(len(arraySet)):
            rank += 1
            map[arraySet[i]] = rank

        for j in range(len(arr)):
            if arr[j] in map:
                result[j] = map[arr[j]]
        return result

    # TC = O(nlogn)
    # SC = O(n)
    def arrayRankTransformHeap(self, arr):
        n = len(arr)
        result = [0] * n
        pq = []
        # store val and its respective index as tuple in heap
        for i, val in enumerate(arr):
            heapq.heappush(pq, (val, i))

        prev = float("inf")
        rank = 0
        # pop elements from the heap
        while pq:
            val, i = heapq.heappop(pq)
            if prev != val:
                rank += 1
                prev = val
                result[i] = rank
            else:
                result[i] = rank
        return result


answer = Solution()
arr = [20, 15, 26, 2, 98, 6]
print(answer.arrayRankTransformBrute(arr))
print(answer.arrayRankTransform(arr))
print(answer.arrayRankTransformHeap(arr))
