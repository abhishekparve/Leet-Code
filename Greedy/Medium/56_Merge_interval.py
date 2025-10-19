class Solution:
    # TC = O(n + n log n)
    # Sc = O(n)
    # Clean Solution --> Neetcode
    def merge(self, intervals):
        # sorting the intervals so that the overlapping
        # intervals appears next to each other
        intervals.sort(key=lambda x: x[0])
        # We are directly append the first interval
        # in the final output this avoids our edge cases
        merged = [intervals[0]]
        for start, end in intervals[1:]:
            # getting the end value of the last merged interval
            # - 1 denotes the last index element
            last = merged[-1][1]
            # If it is over lapping then updating the end value
            # of the last merged interval by taking the max of current end
            # and the existing end value of the merged interval
            if start <= last:
                merged[-1][1] = max(end, last)
            else:
                merged.append([start, end])
        return merged

    # TC = O(n + n log n)
    # Sc = O(n)
    # My Solution with the reference of insert interval problem
    def mergeIntervals(self, intervals):
        result = []
        intervals.sort(key=lambda x: x[0])
        if len(intervals) == 1:
            result.append(intervals[0])
            return result
        # Considering first interval as a new interval
        newInterval = intervals[0]
        # Compaing the other intervals with the new interval
        for i in range(1, len(intervals)):
            if intervals[i][0] <= newInterval[1]:
                newInterval[0] = min(intervals[i][0], newInterval[0])
                newInterval[1] = max(intervals[i][1], newInterval[1])
            else:
                # If an interval is not overlapping with the newInterval
                # 1. first append the newInterval to the result array
                # 2. Make the current interval as the newInterval
                result.append(newInterval)
                newInterval = intervals[i]
        # the last interval will be the newInterval once the for loop is finished
        # so append that interval in the result array
        result.append(newInterval)
        return result


answer = Solution()
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(answer.mergeIntervals(intervals))
print(answer.merge(intervals))
