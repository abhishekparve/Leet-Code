# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

# Example 1:
# Input: nums = [1,1,2]
# Output:
# [[1,1,2], [1,2,1], [2,1,1]]

# Example 2:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

'''The time complexity of this solution is O(n!), where n is the length of the input list nums.
This is because there are n! possible permutations of the input list, and for each permutation,
we perform a constant amount of work (checking if the permutation is complete, adding it to the results list, and backtracking).

The space complexity of this solution is O(n), where n is the length of the input list nums.
This is because we use a count dictionary to keep track of the count of each number in the input list,
and a perms list to store the current permutation. Both of these data structures have a maximum size of n.
Additionally, the results list will store all the permutations, which can have a maximum size of n!.
However, since we are only storing references to the permutations in the results list, the actual space used is O(n).'''


class Solution:
    def permute2(self, nums):
        results = []
        perms = []
        # for count, we can also use an inbuilt function Counter
        # count = Counter(nums)
        count = {n:0 for n in nums}

        for n in nums:
            count[n] += 1

        def dfs():
            if len(perms) == len(nums):
                results.append(perms[:])
                return
            for n in count:
                if count[n] > 0:
                    perms.append(n)
                    count[n] -= 1

                    dfs()
                    count[n] += 1
                    perms.pop()
        dfs()
        return print(results)

answer = Solution()
answer.permute2([1, 1, 2])
            


        