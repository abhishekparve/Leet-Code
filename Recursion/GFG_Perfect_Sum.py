n = 6
arr = [5, 2, 3, 10, 6, 8]
sum = 10


def perfectSum(arr, n, sum):
    # code here
    def backtrack(index, total):
        if total == sum and index == n:
            return 1
        if index >= n or total > sum:
            return 0

        l = backtrack(index + 1, total + arr[index])
        r = backtrack(index + 1, total)
        return l + r

    return backtrack(0, 0)


print(perfectSum(arr, n, sum))
