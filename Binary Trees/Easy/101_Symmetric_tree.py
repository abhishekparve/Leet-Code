class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    # TC = O(n)
    # SC = O(n)
    # Performing reverse preorder on left side
    # Performing preorder on right side
    # Checking both left and right side node simultaneously
    def isSymmetricTree(self, root):
        if root is None:
            return True

        p = root.left
        q = root.right

        def dfs(p, q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            if p.val == q.val and dfs(p.left, q.right) and dfs(p.right, q.left):
                return True
            return False

        return dfs(p, q)


answer = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(2)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(answer.isSymmetricTree(root))
