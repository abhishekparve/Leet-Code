from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    # Using Inorder
    def buildGraphInorder(self, root, parent_map):
        if root is None:
            return
        if root.left:
            parent_map[root.left] = root
        self.buildGraphInorder(root.left)
        if root.right:
            parent_map[root.right] = root
        self.buildGraphInorder(root.right)

    # Using BFS but we can also use DFS traversal
    # TC = O(N) + O(N)
    # SC = O(N) [parent_map]+ O(N)[visited] + O(N)[queue]
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

    def distancek(self, root, target, k):
        self.parent_map = {}
        result = []
        # Step 1 : Building the undirected graph for parent references
        # populating the parent_map using BFS traversal
        self.buildGraph(root, self.parent_map)
        # Created a set to store the visited node
        # so that we won't add the visited node in the queue again
        visited = set()
        # Step 2 : BFS from target node
        queue = deque()
        # Adding the target node to the queue
        queue.append(target)
        visited.add(target.val)
        level_count = 0
        while queue:
            q_size = len(queue)
            if level_count == k:
                break
            for i in range(q_size):
                node = queue.popleft()
                if node.left and node.left.val not in visited:
                    queue.append(node.left)
                    visited.add(node.left.val)
                if node.right and node.right.val not in visited:
                    queue.append(node.right)
                    visited.add(node.right.val)
                # if node is present in parent_map
                # {5 : 3, 6 : 2, 4 : 2}
                # if node is 5, the parent node is 3
                # and self.parent_map[node] ==> what is the parent for that node ?
                # and self.parent_map[node].val == > parent_node.val is not in visited
                if node in self.parent_map and self.parent_map[node].val not in visited:
                    queue.append(self.parent_map[node])
                    visited.add(self.parent_map[node].val)
            level_count += 1
        # Step 3 : Popping the remaining elements from the queue
        #          and storing in the result array
        while queue:
            node = queue.popleft()
            result.append(node.val)
        return result


answer = Solution()
root = TreeNode(3)
root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

target = root.left
k = 2

print(answer.distancek(root, target, k))
