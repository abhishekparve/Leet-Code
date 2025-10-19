from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    # Using BFS
    # TC = O(nlogn)
    # SC = O(n)
    def verticalTraversalBFS(self, root):
        if root is None:
            return [[]]
        queue = deque()
        node_list = []
        queue.append((0, 0, root))
        # row is the horizontal level
        # col is the vertical number line
        # O(n)
        while queue:
            col, row, node = queue.popleft()
            node_list.append((col, row, node.val))
            if node.left:
                queue.append((col - 1, row + 1, node.left))
            if node.right:
                queue.append((col + 1, row + 1, node.right))

        # first sort based on col and then row
        # O(n log(n))
        node_list.sort()
        result = []

        prev_node = float("-inf")
        # O(n)
        for col, row, val in node_list:
            if col != prev_node:
                result.append([])
                prev_node = col
            result[-1].append(val)
        return result

    # Using DFS
    def verticalTraversalDFS(self, root):
        if root is None:
            return [[]]
        node_list = []

        def dfs(col, row, root):
            if root is None:
                return
            node_list.append((col, row, root.val))
            dfs(col - 1, row + 1, root.left)
            dfs(col + 1, row + 1, root.right)

        dfs(0, 0, root)

        node_list.sort()
        result = []
        prev_node = float("-inf")
        for col, row, val in node_list:
            if col != prev_node:
                result.append([])
                prev_node = col
            result[-1].append(val)
        return result


answer = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(answer.verticalTraversalBFS(root))
print(answer.verticalTraversalDFS(root))
