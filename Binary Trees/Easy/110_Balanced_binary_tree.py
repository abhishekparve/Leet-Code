class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    # TC = O(n)
    # SC = O(n)

    # This is a bottom-up approach
    """
    Key Idea:
    i. When computing the height of a node, also check if its subtree is balanced.
    ii. If any subtree is not balanced, propagate -1 upward to signal that the whole tree is not balanced.
    iii. This avoids redundant re-computation and unnecessary traversal.
    """

    """
    Think like:

    Imagine you're a tree node. You ask your left and right children:

    “Hey, what’s your height?”
    If either child says: “I’m not balanced” (returns -1), then you immediately return -1 too.
    Otherwise, you compare both heights. If the difference is more than 1, you return -1.

    If everything's fine, you return your height as 1 + max(left, right).
    """

    def isBalancedOptimal(self, root):
        def checkHeight(root):
            if root is None:
                return 0
            l_height = checkHeight(root.left)
            if l_height == -1:
                return -1
            r_height = checkHeight(root.right)
            if r_height == -1:
                return -1

            if abs(l_height - r_height) > 1:
                return -1

            return 1 + max(l_height, r_height)

        return checkHeight(root) != -1

    # TC = O(n^2)
    # SC = O(n)
    """
    What's the Problem?

    For every node, you recompute the height of its subtrees.

    So for n nodes, you end up doing height calculations repeatedly — resulting in O(n²)
    time complexity in the worst case (like a skewed tree).
    """

    def isBalancedBrute(self, root):
        # A empty tree is also a balanced binary tree
        if root is None:
            return True

        # Computing the height of the tree
        def checkHeight(root):
            if root is None:
                return 0

            l_height = checkHeight(root.left)
            r_height = checkHeight(root.right)

            return 1 + max(l_height, r_height)

        # Here we are checking for every node if that subtree is balanced or not
        left_height = checkHeight(root.left)
        right_height = checkHeight(root.right)

        if abs(left_height - right_height) > 1:
            return False
        # We are recursively validating that every subtree in the tree is also balanced — not just the root node.
        # Here we are checking if the overall left subtree of the root and right subtree of the root is balanced or not
        return self.isBalancedBrute(root.left) and self.isBalancedBrute(root.right)


answer = Solution()
# root = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.left.right.left = TreeNode(6)
root.left.right.right = TreeNode(7)

root.right.left = TreeNode(9)
root.right.right = TreeNode(8)

print(answer.isBalancedBrute(root))
print(answer.isBalancedOptimal(root))
