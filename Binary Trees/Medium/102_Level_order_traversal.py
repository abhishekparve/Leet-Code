from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    # This is the BFS (Breadth First Search) which is implemented using the queue data structure
    # TC = O(n)
    # SC = O(n)
    def levelOrder(self, root):
        if root is None:
            return []
        # queue = collections.deque()
        queue = deque()
        # 1. Initially append the root node to the queue
        queue.append(root)
        result = []
        # loop until the queue is empty
        # You store the current size of the queue (q_size), which corresponds to the
        # number of nodes in the current level.

        # we then process exactly q_size nodes (all nodes at that level).
        # As we process each node, you:
        # i. Record its value.
        # ii. Enqueue its children for the next level.
        while queue:
            level = []
            q_size = len(queue)
            for i in range(q_size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # Append the entire level in the result array
            result.append(level)
        return result


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

print(answer.levelorder(root))
