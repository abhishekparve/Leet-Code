from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    # Same code as level order traversal just we have introduced flag
    # When left_to_right flag is true store the node values in left to right fashion
    # when left_to_right flag is false store the node values in right to left (reverse) fashion
    # TC = O(n)
    # SC = O(n)
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        result = []
        queue = deque()
        queue.append(root)
        left_to_right = True
        while queue:
            size = len(queue)
            level = [0] * size
            for i in range(len(queue)):
                node = queue.popleft()
                # size - 1 - i : mirror image index of i
                index = i if left_to_right else size - 1 - i
                level[index] = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # Reset the flag after every for loop
            left_to_right = not left_to_right
            result.append(level)
        return result


answer = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(answer.zigzagLevelOrder(root))
"""
why size - 1 - i ?

lets say size = 4
i      node       desired index
0       A             3
1       B             2
2       C             1
3       D             0

for i = 0, 4 - 1 - 0 = 3
for i = 1, 4 - 1 - 1 = 2
for i = 2, 4 - 1 - 2 = 1
for i = 3, 4 - 1 - 3 = 4

size - 1: Gives you the last index of the array (since lists are 0-indexed).
i: Is the position you're currently processing left to right.
Subtracting i from size - 1 gives you the mirror image index from the right.
"""
