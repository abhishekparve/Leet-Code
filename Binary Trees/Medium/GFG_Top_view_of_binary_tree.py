from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    # TC = O(nlogn)
    # SC = O(2n)
    """
    Using a BFS traversal (deque) to traverse the tree level by level.
    The hd variable tracks the horizontal distance (HD) from the root.
    The use of a hash_map to store the first node at each horizontal distance ensures that you get the topmost node from that column.
    """

    # hd represents the horizontal distance on the number line scale
    # -2 -1 0 1 2
    def topViewOfBinaryTree(self, root):
        if root is None:
            return []
        queue = deque()
        hd_map = {}
        queue.append((0, root))
        while queue:
            hd, node = queue.popleft()
            if hd not in hd_map:
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

    # O(n log n) can be avoided if we maintain two variables for min horizontal distance
    # and max horizontal distance

    def topViewOfBinaryTreeOptimal(self, root):
        if root is None:
            return []
        queue = deque()
        hd_map = {}
        # hd = horizantal distance
        queue.append((0, root))
        min_hd = 0
        max_hd = 0
        while queue:
            hd, node = queue.popleft()
            if hd not in hd_map:
                hd_map[hd] = node.val
            if node.left:
                queue.append((hd - 1, node.left))
            if node.right:
                queue.append((hd + 1, node.right))
            # calculating the min and max horizontal distance for the range after popping every node from the queue
            min_hd = min(min_hd, hd)
            max_hd = max(max_hd, hd)

        result = []
        for i in range(min_hd, max_hd + 1):
            result.append(hd_map[i])
        return result


answer = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.left.right.right = TreeNode(5)
root.left.right.right.right = TreeNode(6)
print(answer.topViewOfBinaryTree(root))
print(answer.topViewOfBinaryTreeOptimal(root))


"""
Q. Why don't we use DFS instead of BFS?

With DFS, you might overwrite a top node if a deeper node is visited first — this needs extra checks.
So BFS is better suited for top view — because it naturally prioritizes topmost nodes.

"""
