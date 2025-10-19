from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    # In bottom view approach:
    # Since BFS visits nodes level by level, later nodes at the same HD will overwrite earlier ones —
    # which is exactly what we want for the bottom view.

    # TC = O(n logn)
    # SC = O(n)
    def bottomViewOfBinaryTree(self, root):
        if root is None:
            return []
        queue = deque()
        hd_map = {}
        queue.append((0, root))
        while queue:
            hd, node = queue.popleft()
            hd_map[hd] = node.val
            if node.left:
                queue.append((hd - 1, node.left))
            if node.right:
                queue.append((hd + 1, node.right))

        result = []
        # Iterating, Pushing and poping elements in queue = O(n)
        # sorting hash_map if at worst case there are n key = O(nlogn)
        # Iterating hash_map = O(n)

        # SC = O(2n)
        # O(n) space for hash_map
        # O(n) space for result
        for key in sorted(hd_map.keys()):
            result.append(hd_map[key])
        return result

    # TC = O(n)
    # SC = O(n)
    def bottomViewOfBinaryTreeOptimal(self, root):
        if root is None:
            return []
        min_hd = 0
        max_hd = 0
        hd_map = {}
        queue = deque()
        queue.append((0, root))
        while queue:
            hd, node = queue.popleft()
            hd_map[hd] = node.val
            if node.left:
                queue.append((hd - 1, node.left))
            if node.right:
                queue.append((hd + 1, node.right))

            min_hd = min(min_hd, hd)
            max_hd = max(max_hd, hd)

        result = []

        for i in range(min_hd, max_hd + 1):
            result.append(hd_map[i])

        return result


answer = Solution()
root = TreeNode(10)
root.left = TreeNode(20)
root.left.left = TreeNode(40)
root.left.right = TreeNode(60)
root.right = TreeNode(30)

print(answer.bottomViewOfBinaryTree(root))
print(answer.bottomViewOfBinaryTreeOptimal(root))
