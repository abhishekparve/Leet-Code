from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    # Watch Striver
    def maxWidth(self, root):
        queue = deque()
        queue.append((root, 0))  # [node, index]
        max_width = 0
        while queue:
            # getting the first index from the begining of the queue
            first_index = queue[0][1]
            # getting the last index from the end of the queue
            last_index = queue[-1][1]
            # gettting the min_index at that level which will be same as first_index
            min_index = queue[0][1]
            q_size = len(queue)
            max_width = max(max_width, last_index - first_index + 1)
            for i in range(q_size):
                node, curr_index = queue.popleft()
                # Subtracting the current index by the min_index to avoid overflow
                # can also do it as
                # index -= first_index
                index = curr_index - min_index
                if node.left:
                    queue.append((node.left, 2 * index + 1))
                if node.right:
                    queue.append((node.right, 2 * index + 2))
        return max_width


answer = Solution()
root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.right.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)

print(answer.maxWidth(root))
