from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    # TC = O(3N)
    # SC = O(3N)
    def buildGraph(self, root, parent_map):
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.left:
                parent_map[node.left] = node
                queue.append(node.left)
            if node.right:
                parent_map[node.right] = node
                queue.append(node.right)

    def findNode(self, root, target):
        if root == None:
            return
        if root.val == target:
            return root
        left = self.findNode(root.left, target)
        right = self.findNode(root.right, target)
        if left:
            return left
        if right:
            return right

    # Same solution as all nodes distance K in binary tree
    # and GFG Burning Tree
    def amountOfTime(self, root, start):
        self.parent_map = {}
        self.buildGraph(root, self.parent_map)
        visited = set()
        queue = deque()
        target_node = self.findNode(root, start)
        queue.append(target_node)
        visited.add(target_node)
        time = 0
        while queue:
            q_size = len(queue)
            spread = False
            for i in range(q_size):
                node = queue.popleft()
                if node.left and node.left not in visited:
                    queue.append(node.left)
                    visited.add(node.left)
                    spread = True
                if node.right and node.right not in visited:
                    queue.append(node.right)
                    visited.add(node.right)
                    spread = True
                if node in self.parent_map and self.parent_map[node] not in visited:
                    queue.append(self.parent_map[node])
                    visited.add(self.parent_map[node])
                    spread = True

            if spread:
                time += 1

        return time

    # TC = O(N)
    # CodeStory Solution
    def amountOfTimeDFS(self, root, start):
        time = 0

        def dfs(root):
            if root is None:
                return 0

            LH = self.amountOfTimeDFS(root.left, start)
            RH = self.amountOfTimeDFS(root.left, start)

            if root.val == start:
                time = max(LH, RH)
                return -1
            elif LH > 0 and RH > 0:
                return max(LH, RH) + 1
            else:
                distance = abs(LH) + abs(RH)
                time = max(time, distance)
                return min(LH, RH) - 1

        return dfs(root)
