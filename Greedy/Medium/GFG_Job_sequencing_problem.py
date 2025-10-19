from operator import itemgetter


class Solution:
    # TC
    """
    O(n)            # job list creation
    + O(n log n)    # sorting by profit
    + O(n)          # max deadline
    + O(D)          # slots initialization
    + O(n * D)      # scheduling jobs
    -------------------------------
    = O(n log n + n * D)
    """

    def jobSequencing(self, deadline, profit):
        # O(n)
        jobs = [[deadline[i], profit[i]] for i in range(len(profit))]
        # We sort the jobs in reverse order based on highest profit greedily
        # O(n log n)
        jobs.sort(key=itemgetter(1), reverse=True)
        # O(n)
        max_deadline = max(deadline)
        # We are not using index = 0
        # because there is no deadline zero and our evaluation
        # becomes easy
        slots = [-1] * (max_deadline + 1)  # O(max(deadline))
        max_profit = 0
        job_count = 0
        # outer loop = O(n)
        for d, p in jobs:
            # Worst case: all d = D → inner loop runs D times per job.
            # The inner loop can be optimized using DSU - > dis joint unit (topic of graph)
            for i in range(d, 0, -1):
                if slots[i] == -1:
                    slots[i] = d
                    job_count += 1
                    max_profit += p
                    break

        return [job_count, max_profit]


answer = Solution()
deadline = [2, 1, 2, 1, 1]
profit = [100, 19, 27, 25, 15]
print(answer.jobSequencing(deadline, profit))

"""
What is the purpose of the for loop?

For each job (d, p):

It tries to find the latest free slot on or before its deadline d.
If such a slot exists, the job is scheduled there.
This maximizes the chance that earlier slots remain available for other jobs with smaller deadlines.

This is a classic greedy scheduling technique.
"""
"""
Why do we try to assign each job to the latest available slot before its deadline?

We assign a job to the latest possible slot before its deadline to leave earlier slots open
for other jobs that must be done earlier (i.e. jobs with tighter deadlines). This increases 
the total number of jobs we can schedule, thereby potentially increasing total profit.

jobs = [(2, 100), (1, 50), (2, 20)]
Suppose we assign jobs to the earliest available slot, here's what might happen:

Job (2, 100) → assign to slot 1 (earliest available)

Job (1, 50) → slot 1 is taken → cannot assign

Job (2, 20) → assign to slot 2

✅ Total jobs = 2, Profit = 100 + 20 = 120

Now Try Latest Slot First (Correct Greedy Strategy):
Job (2, 100) → assign to slot 2 (latest possible)

Job (1, 50) → assign to slot 1

Job (2, 20) → no slot left → can't assign

✅ Total jobs = 2, Profit = 100 + 50 = 150

🚀 Higher profit and same number of jobs.

"""
