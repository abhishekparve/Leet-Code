# Question : https://www.geeksforgeeks.org/problems/sort-a-stack/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=sort-a-stack


# TC = O(N^2) SC = O(1)
class Solution:
    def sort(self, stack):
        if not stack:
            return
        top = stack.pop()
        self.sort(stack)
        self.insert(stack, top)

    def insert(self, stack, elem):
        if not stack or stack[-1] <= elem:
            stack.append(elem)
            return
        top = stack.pop()
        self.insert(stack, elem)
        stack.append(top)


stack = [11, 2, 32, 3, 41]
answer = Solution()
answer.sort(stack)
print(stack)
