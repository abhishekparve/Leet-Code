# https://www.geeksforgeeks.org/the-celebrity-problem/


class Solution:
    # TC = O(n^2) + O(n)
    # SC = O(2n)
    def celebrityBrute(self, mat):
        # since it is n * n matrix
        n = len(mat)
        knowMe = [0] * n
        iKnow = [0] * n
        for i in range(n):
            for j in range(n):
                # The same person knows himself does not make any sense
                # so if i == j then continue
                if i == j:
                    continue
                if mat[i][j] == 1:
                    knowMe[j] += 1
                    iKnow[i] += 1
        print(knowMe)
        print(iKnow)
        # A celebrity is the person who is knownby all but he knows no one
        # n - 1 becz except him rest everyone should know him
        # 0 bcz he should know no one
        for i in range(n):
            if knowMe[i] == n - 1 and iKnow[i] == 0:
                return i
        return -1

    # TC = O(n)
    # SC = O(1)
    def celebrityOptimal(self, mat):
        # Two pointers
        n = len(mat)
        top = 0
        bottom = n - 1
        while top < bottom:
            if mat[top][bottom] == 1:
                top += 1
            else:
                bottom -= 1

        candidate = top

        for i in range(n):
            if i == candidate:
                continue
            if mat[candidate][i] == 1 or mat[i][candidate] == 0:
                return -1
        return top


answer = Solution()
mat = [[1, 1, 0], [0, 1, 0], [0, 1, 1]]
print(answer.celebrityBrute(mat))
print(answer.celebrityOptimal(mat))
