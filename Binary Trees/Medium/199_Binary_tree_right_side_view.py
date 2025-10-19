from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    # storing the row value in the queue and hash_map
    # TC = O(n)
    # SC = O(n)
    def rightSideViewLevelOrder(self, root):
        if root is None:
            return []
        queue = deque()
        dist_map = {}
        queue.append((0, root))
        min_dist = 0
        max_dist = 0
        while queue:
            d, node = queue.popleft()
            # left side nodes will be overriden by the extreme right ones
            dist_map[d] = node.val
            if node.left:
                queue.append((d + 1, node.left))
            if node.right:
                queue.append((d + 1, node.right))
            min_dist = min(min_dist, d)
            max_dist = max(max_dist, d)

        result = []
        for i in range(min_dist, max_dist + 1):
            result.append(dist_map[i])
        return result

    # Reverse Preorder Traversal
    # Preorder traversal is Root Left Right
    # but in below approach we will smartly check Root Right Left
    # we are checking right because from the right end it is the very first node
    # if we take a look from right size
    # TC = O(n)
    # SC = O(h)
    def rightSideViewReversePreorder(self, root):
        self.result = []
        if root is None:
            return []

        def preOrder(root, level):
            if root is None:
                return
            # If the length of the data structure is equal to the level
            # we will add the node value in the data structure
            if level == len(self.result):
                self.result.append(root.val)
            preOrder(root.right, level + 1)
            preOrder(root.left, level + 1)

        preOrder(root, 0)
        return self.result


"""
Since we are calling the dfs function on the right side first the right side node
values will be stored in the data structure first and by the time we recursively
come towards the left section of the tree, the data structure size will already be 
equal to the max depth of the right section. So the level for the left section
will never match the length the DS unless we exceed the max depth of the right section.
"""

answer = Solution()
root = TreeNode(1)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
root.left = TreeNode(2)
root.left.right = TreeNode(5)

print(answer.rightSideViewLevelOrder(root))
print(answer.rightSideViewReversePreorder(root))
