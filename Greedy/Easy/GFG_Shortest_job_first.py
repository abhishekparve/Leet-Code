class Solution:
    # burst time is the total amount of time a process requires to complete its execution on the CPU,
    # excluding any time spent waiting in queues
    """
    1. Completion Time: Time at which process completes its execution.
    2. Turn Around Time: Time Difference between completion time and arrival time.
        Turn Around Time = Completion Time - Arrival Time
    3. Waiting Time(W.T): Time Difference between turn around time and burst time.
        Waiting Time = Turn Around Time -  Burst Time

    Consider the processes [2, 3]
    for both these processes the arrival time is zero
    As per SJF, process 2 gets executed. Therefore completion time = 2
    and then process 3 gets exectued. Therefore the completion time = 2 + 3 = 5 and so on..
    """

    # In the below example we are not calculating the turn around time bcz for
    # each process the arrival time is zero. So the subraction of CT with the arrival time will
    # have not effect. Here the TAT is equal to completion time

    # TC = O(2n + n*logn)
    # SC = O(n)
    def avgWaitingTimeBrute(self, bt):
        n = len(bt)
        completion_time = [0] * n
        waiting_time = 0
        # Sorting the array becausing in SJF the jobs with smallest burst time
        # gets executed first
        bt.sort()
        current_time = 0
        for i in range(n):
            current_time += bt[i]
            completion_time[i] = current_time

        for i in range(len(completion_time)):
            waiting_time += completion_time[i] - bt[i]

        return waiting_time // n

    # TC = O(n + n*logn)
    # SC = O(1)
    def avgWaitingTime(self, bt):
        n = len(bt)
        # O(n logn)
        bt.sort()
        waiting_time = 0
        completion_time = 0
        # O(n)
        for i in range(n):
            waiting_time += completion_time
            completion_time += bt[i]
        return waiting_time // n


answer = Solution()
bt = [4, 3, 7, 1, 2]
print(answer.avgWaitingTimeBrute(bt))
print(answer.avgWaitingTime(bt))
