class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTreeBrute(self, root):
        if root is None:
            return 0

        def getHeight(root):
            if root is None:
                return 0

            l_height = getHeight(root.left)
            r_height = getHeight(root.right)

            return 1 + max(l_height, r_height)

        l_height = getHeight(root.left)
        r_height = getHeight(root.right)

        diameter_for_node = l_height + r_height

        diameter_for_subtree = max(
            self.diameterOfBinaryTreeBrute(root.left),
            self.diameterOfBinaryTreeBrute(root.right),
        )

        return max(diameter_for_node, diameter_for_subtree)

    # Optimal
    # TC = O(n)
    # SC = O(n) ==> not auxillary(extra) space but the stack space
    def diameterOfBinaryTree(self, root):
        self.result = 0

        if root is None:
            return 0
        self.getHeight(root)
        return self.result

    def getHeight(self, root):
        if root is None:
            return 0

        l_height = self.getHeight(root.left)
        r_height = self.getHeight(root.right)

        self.result = max(self.result, l_height + r_height)

        return 1 + max(l_height, r_height)


# In the brute force we were calculating the height of each node and storing max of them in one variable
# and then calculating the max height of left and right subtrees and storing the max of them in another variable
# then we were returning the max out of these two variables as result
# With that approach we were doing lot of repetative recursion
# In the below optimal approach we will declare one global variable to store the max diameter

# And once we calculate the height of a subtree at the same time we will also calculate
# the maximum diameter we have got till that point and store it in result

# NOTE : The getHeight method is just calculating the height for that particular node but while
# doing so we are also updating the maximum diameter we have got till that point and store it in result

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

print(answer.diameterOfBinaryTreeBrute(root))
print(answer.diameterOfBinaryTree(root))
