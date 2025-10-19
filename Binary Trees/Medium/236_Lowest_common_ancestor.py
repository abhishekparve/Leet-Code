class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    # TC = O(n)
    # SC = O(n)
    """
    If the left subtree recursive call gives a null value that means we haven’t found LCA in the left subtree, which means we found LCA on the right subtree. So we will return right.
    If the right subtree recursive call gives null value, that means we haven’t found LCA on the right subtree, which means we found LCA on the left subtree. So we will return left .
    If both left & right calls give values (not null)  that means the root is the LCA.
    """

    def lowestCommonAncestor(self, root, p, q):
        if root is None:
            return
        # In this if you find weather the p or q
        # You return the node itself
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        elif left:
            return left
        else:
            return right

    # TC = O(n)
    # SC = O(2n)
    def lowestCommonAncestorBrute(self, root, p, q):
        path1 = []
        path2 = []

        # In dfs:
        # case 1 : If root is equal to p or q ===> return True
        # case 2 : If from the left section we get a node equal to p or q
        #         OR from the right section we get a node equal to p or q
        #         we return True because a node can be an ancestor of itself
        def dfs(root, path, k):
            if root is None:
                return
            path.append(root)

            if root == k:
                return True
            if dfs(root.left, path, k) or dfs(root.right, path, k):
                return True
            return False

        # getting the path for p in path1 array
        dfs(root, path1, p)
        # getting the path for q in path2 array
        dfs(root, path2, q)

        i = 0
        # Initializing lowest common ancestor
        lca = None
        while i < len(path1) and i < len(path2):
            if path1[i] == path2[i]:
                lca = path1[i]
            else:
                break
            i += 1
        return lca


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

p = 7
q = 4
print(answer.lowestCommonAncestorBrute(root, p, q))
print(answer.lowestCommonAncestor(root, p, q))
