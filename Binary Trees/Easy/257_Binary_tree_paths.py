class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    # TC = O(n)
    # SC = O(n)
    def binaryTreePathsArray(self, root):
        self.result = []
        if root is None:
            return []

        def dfs(root, path):
            if root is None:
                return
            path.append(str(root.val))
            # If it is a leaf node
            # join the path with "->" and append it to the result
            if root.left is None and root.right is None:
                self.result.append("->".join(path))
            else:
                dfs(root.left, path)
                dfs(root.right, path)
            # backtrack
            path.pop()

        dfs(root, [])
        return self.result

    # TC = O(n)
    # SC = O(n)
    def binaryTreePathsString(self, root):
        self.result = []
        if root is None:
            return []

        def dfsWithString(root, path):
            if root is None:
                return []
            path += str(root.val)
            # If it is a leaf node
            # append the path in the result
            if root.left is None and root.right is None:
                self.result.append(path)
            else:
                dfsWithString(root.left, path + "->")
                dfsWithString(root.right, path + "->")
            # No need to pop bcz a new path string is created at each call

        dfsWithString(root, "")
        return self.result


answer = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)

print(answer.binaryTreePathsArray(root))
print(answer.binaryTreePathsString(root))
