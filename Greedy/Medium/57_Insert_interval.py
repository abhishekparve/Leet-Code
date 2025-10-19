class Solution:
    # TC = O(n)
    # SC = O(n)
    # Code Story solution
    def insertIntervalCS(self, intervals, newInterval):
        n = len(intervals)
        i = 0
        result = []
        while i < n:
            # If end of the interval is less than the start of the newInterval
            # which means that the current interval has already ended. So append it
            # to the result and move to the next
            if intervals[i][1] < newInterval[0]:
                result.append(intervals[i])
                i += 1
            # If the start of the interval is greater than the end of the newInterval
            # which means that the current interval comes way after the newInterval and it does not overlap
            # so we break out of the loop because since the array is already sorted anything
            # after the the current interval will never overlap with the newInterval
            elif intervals[i][0] > newInterval[1]:
                break
            # Overlapping condition
            # Intervals ==> 3-----5, 6----10
            # newInterval ==> 4---8
            # Since we need a complete range we take the
            # min of start of newInterval and the start of the current interval and
            # max of end of newInterval and the end of the current interval
            # so range becomes 3 ----- 10
            else:
                newInterval[0] = min(intervals[i][0], newInterval[0])
                newInterval[1] = max(intervals[i][1], newInterval[1])
                i += 1

        result.append(newInterval)
        # due to the break condition if there are some intervals
        # that are left we straight up add it to the result
        while i < n:
            result.append(intervals[i])
            i += 1
        return result

    # TC = O(n)
    # SC = O(n)
    def insertIntervalStriver(self, intervals, newInterval):
        i = 0
        n = len(intervals)
        result = []
        # First part
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Overlapping part
        # merging intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1

        # Append the newInterval in case no overlapping is found or
        # you have got the newInterval range by merging intervals
        result.append(newInterval)

        # last section
        while i < n:
            result.append(intervals[i])
            i += 1
        return result


answer = Solution()
intervals1 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval1 = [4, 8]
print(answer.insertIntervalCS(intervals1, newInterval1))
intervals2 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval2 = [4, 8]
print(answer.insertIntervalStriver(intervals2, newInterval2))
