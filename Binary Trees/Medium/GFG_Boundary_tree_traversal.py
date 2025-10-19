class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    # TC = O(n) (inorder leaf node traversal) + O(h)(left boundary traversal) + O(h) (right boundary traversal) ~ O(n)
    # SC = O(n) (result) + O(n) (Recursive stack space)
    def isLeaf(self, root):
        return root.left is None and root.right is None

    # Collect all the leaf node in left to right order
    # Inorder traversal
    def leafNodeTraversal(self, root):
        if root is None:
            return
        if self.isLeaf(root):
            self.result.append(root.val)
        self.leafNodeTraversal(root.left)
        self.leafNodeTraversal(root.right)

    # Go as left as possible.
    # Ignore leaves here to avoid duplication when you collect all leaves later.
    def leftBoundaryTraversal(self, root):
        curr = root.left
        while curr:
            if not self.isLeaf(curr):
                self.result.append(curr.val)
            if curr.left:
                curr = curr.left
            # If left not present go right
            else:
                curr = curr.right

    # Go as right as possible.
    # Ignore leaves here to avoid duplication when you collect all leaves later.
    # Since we are walking anti-clockwise, store in a stack or list and reverse
    def rightBoundaryTraversal(self, root):
        stack = []
        curr = root.right
        while curr:
            if not self.isLeaf(curr):
                stack.append(curr.val)
            if curr.right:
                curr = curr.right
            # If right not present go left
            else:
                curr = curr.left

        while stack:
            data = stack.pop()
            self.result.append(data)

    # Root + Left Boundary + Leaves + Reversed Right Boundary
    def boundaryTraversal(self, root):
        if root is None:
            return []
        self.result = []
        if not self.isLeaf(root):
            self.result.append(root.val)
        self.leftBoundaryTraversal(root)
        self.leafNodeTraversal(root)
        self.rightBoundaryTraversal(root)
        return self.result


answer = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.right = TreeNode(4)
root.left.left.right.left = TreeNode(5)
root.left.left.right.right = TreeNode(6)

root.right = TreeNode(7)
root.right.right = TreeNode(8)
root.right.right.left = TreeNode(9)
root.right.right.left.left = TreeNode(10)
root.right.right.left.right = TreeNode(11)

print(answer.boundaryTraversal(root))

"""
In boundary traversal, you want to traverse the tree along its outer edge, in anti-clockwise direction,
collecting node values without repetition.

This includes:

1. Left boundary (excluding leaf nodes)
2. All leaf nodes (from left to right)
3. Right boundary (excluding leaf nodes, in reverse order)

Why Do We Split It?

i. We split into 3 parts (left, leaves, right) to:
ii. Avoid duplicate leaves (especially in skewed trees)
iii. Maintain correct order (left boundary top-down, right boundary bottom-up)

Make traversal modular and easier to debug.
"""
