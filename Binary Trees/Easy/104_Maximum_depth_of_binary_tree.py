from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        l_height = self.maxDepth(root.left)
        r_height = self.maxDepth(root.right)

        return 1 + max(l_height, r_height)

    def maxDepthBFS(self, root):
        if root is None:
            return 0
        queue = deque()
        queue.append(root)
        level = 0
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return level

    def maxDepthDFS(self, root):
        if root is None:
            return 0
        stack = [[root, 1]]
        level = 0
        while stack:
            node, depth = stack.pop()
            level = max(level, depth)
            if node.left:
                stack.append([node.left, depth + 1])
            if node.right:
                stack.append([node.right, depth + 1])
        return level


answer = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.left.right.left = TreeNode(6)
root.left.right.right = TreeNode(7)

root.right.left = TreeNode(9)
root.right.right = TreeNode(8)

print(answer.maxDepth(root))
print(answer.maxDepthBFS(root))
print(answer.maxDepthDFS(root))
