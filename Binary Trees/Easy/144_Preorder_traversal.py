class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    # Root, Left, Right
    # TC = O(n)
    # SC = O(h) ==> h is the height of the tree
    # best case height for balanced tree ==> O(logn)
    # Worst case for skewed tree == > O(n)
    def preorderTraversalRecursive(self, root):
        if root is None:
            return []

        result = [root.val]
        result += self.preorderTraversalRecursive(root.left)
        result += self.preorderTraversalRecursive(root.right)
        return result

    # Itervative approach
    # TC = O(n)
    # SC = O(h)
    def preorderTraversalIterative(self, root):
        if root is None:
            return []
        # Initially push the root node in the stack if it is not null
        stack = [root]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.val)
            # Push right node first and then the left node
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result


"""
Q. Why Push Right First, Then Left?

Stacks are Last In, First Out (LIFO) — the last thing you push is the first thing that gets popped.
Since preorder requires us to visit the left child before the right, we need the left child to be
on top of the stack, so it's processed first.

So we:
Push the right child first → it goes to the bottom.
Push the left child next → it goes on top.

That way, when we pop(), we get the left child before the right child, maintaining the correct
traversal order.
"""


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
print(answer.preorderTraversalRecursive(root))
print(answer.preorderTraversalIterative(root))
