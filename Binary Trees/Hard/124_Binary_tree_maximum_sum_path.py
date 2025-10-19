class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    # TC = O(n)
    # SC = O(n)
    def findMaximumSumPath(self, root):
        # global variable to store the max path
        self.result = float("-inf")

        def dfs(root):
            if root is None:
                return 0
            # we are taking the max bcz both the children for the node might
            # be negative and we do not want to include as the root value itself gives
            # us a positive answer. So if either of the leftMax or rightMax return us a
            # negative value we always return 0. As a result even if we add the leftMax and rightMax
            # to the root.val it will not affect the self.result max value
            leftMax = max(0, dfs(root.left))
            rightMax = max(0, dfs(root.right))

            # max path with the split
            # including the curve '^'
            self.result = max(self.result, root.val + leftMax + rightMax)

            # max path without the split
            # without the curve '\' or'/'
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return self.result


answer = Solution()

root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(answer.findMaximumSumPath(root))
