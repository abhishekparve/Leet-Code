class Solution:
    # Whenever you see something related to intervals
    # 1. first try sorting based on start time
    # 2. Then try sorting based on end time
    # NOTE : Same as the max meetings in one room problem
    # TC = O(n + n log n)
    # SC = O(1)
    def eraseOverlappingIntervals(self, intervals):
        # there will be atleast one meeting. So count = 1
        # Any which ways this will be subtracted to 0 if there is only one interval.
        count = 1
        n = len(intervals)
        intervals.sort(key=lambda x: x[1])
        last_end = intervals[0][1]
        # Counting all the non-overlapping intervals
        for start, end in intervals[1:]:
            # non-overlapping condition
            if start >= last_end:
                count += 1
                last_end = end
            # if over lapping then skip
        # overlapping intervals to delete = (Total intervals - non-overlapping intervals)
        return n - count


answer = Solution()
intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(answer.eraseOverlappingIntervals(intervals))
