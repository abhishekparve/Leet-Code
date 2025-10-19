from collections import deque

# https://www.geeksforgeeks.org/problems/children-sum-parent/1


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def isSumProperty(self, root):
        if root is None or (root.left is None and root.right is None):
            return True

        sum = 0
        if root.left:
            sum += root.left.val
        if root.right:
            sum += root.right.val

        if (
            root.val == sum
            and self.isSumProperty(root.left)
            and self.isSumProperty(root.right)
        ):
            return True
        else:
            return False

    def isSumPropertyBFS(self, root):
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            sum = 0
            # If the node is leaf node
            if node.left is None and node.right is None:
                continue

            if node.left:
                sum += node.left.val

            if node.right:
                sum += node.right.val

            # If the parent node value is not equal to the sum of both of
            # its child return False
            if node.val != sum:
                return False

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return True

    # Similar problem for child sum property
    # https://www.geeksforgeeks.org/dsa/convert-an-arbitrary-binary-tree-to-a-tree-that-holds-children-sum-property/
    # Optimal Solution -- Striver
    # Check brute force later
    # TC = O(N)
    # SC = O(H)

    def convert(self, root):
        if root is None or (root.left is None and root.right is None):
            return

        child_sum = 0
        if root.left:
            child_sum += root.left.val
        if root.right:
            child_sum += root.right.val
        # if sum of child nodes is greater than parent then update the
        # parent node
        if child_sum >= root.val:
            root.val = child_sum
        # if sum of child nodes is less than parent then update the
        # child nodes with the parent node value
        elif child_sum < root.val:
            if root.left:
                root.left = root.val
            if root.right:
                root.right = root.val

        # recursive call to the left
        self.convert(root.left)
        # recursive call to the right
        self.convert(root.right)

        # While coming back from the recursion
        total = 0
        if root.left:
            total += root.left.val
        if root.right:
            total += root.right.val
        # If the node is not a leaf node then only update the parent node
        if root.left or root.right:
            root.val = total


answer = Solution()

root = TreeNode(35)
root.left = TreeNode(20)
root.left.left = TreeNode(15)
root.left.right = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

print(answer.isSumProperty(root))
print(answer.isSumPropertyBFS(root))
