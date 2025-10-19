from operator import itemgetter


class Solution:
    # TC = O(n + n logn + n)
    # Sc = O(n)
    # Approach:
    # Our goal is to:
    # Select the maximum number of meetings such that no two meetings overlap.
    # Only one meeting can happen at a time
    # Lets assume
    # meeting  A  B  C
    # start = [1, 2, 3]
    # end   = [3, 4, 5]
    # If we pick meeting A (1, 3) we are also able to pick meeting C (3, 5) because the don't overlap
    # But if we pick meeting B (2, 4), we will not be able to pick any other meeting
    # Always choose the meeting that finishes the earliest — this leaves as much room as possible for the rest.
    def maxNumberOfMeetings(self, start, end):
        # we are keeping end value at the first index because there can be case where the
        # end time of two or more meetings might be same. So the tuple can then compare the next element
        # at index 1 (start time) for sorting
        # TC = O(n)
        time = [(end[i], start[i]) for i in range(len(start))]
        # TC = O(n log n)
        time.sort(key=itemgetter(0))

        last_end_time = -1
        meetings = 0
        # TC = O(n)
        for e, s in time:
            # If the start time of the new meeting is greater than the last_end_time
            # it means that the room is idle and the room can be allocated now.
            if last_end_time < s:
                last_end_time = e
                meetings += 1
        return meetings


# Why -1 instead of 0?
# for last_end_time = 0
# This means that the room is busy until 0 time
# If there's a meeting that starts at time 0, it will be skipped

# On the other hand, if last_end_time = -1:
# You are saying --
# “No meeting has happened yet — the room is available from the very beginning.”

answer = Solution()
start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]
print(answer.maxNumberOfMeetings(start, end))
