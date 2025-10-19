class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def isSame(self, p, q):
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        return (
            p.val == q.val
            and self.isSame(p.left, q.left)
            and self.isSame(p.right, q.right)
        )


answer = Solution()
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

print(answer.isSame(p, q))
