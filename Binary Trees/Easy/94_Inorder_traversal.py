class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def inorderTraversalRecursion(self, root):
        result = []

        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            result.append(root.val)
            inorder(root.right)

        inorder(root)
        return result

    # TC = O(n)
    # SC = O(n)
    def inorderTraversalStack(self, root):
        if root is None:
            return []
        stack = []
        result = []
        # Keeping the pointer at the root
        curr = root
        # Keeping moving the curr pointer towards
        # the left until the curr pointer reaches null
        # and parallelly also append the curr node to the stack
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            # At this stage the curr is null
            # then pop the node from stack and append its value to the result then
            # move the curr pointer to the right node of the popped node
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        return result

    # TC = O(n)
    # SC = O(1)
    # NOTE :DO NOT REFER TO THE LEETCODE SUBMITTED CODE. IT has bunch of issues we are modifying the tree
    # there which might break. REFER BELOW CODE.
    # Morris Traversal
    # What morris say's is if there is a root.left (leftNode) node
    # then check whether the leftNode has a child right node(root.left.right)
    # If YES,
    # then keeping moving towards the right MOST node of the leftNode
    # and connect that right most node (root.left.right) to the root node
    # and then break the link between the root node and the leftNode by using a temp
    # IF the leftNode (root.left) is not present append the rootNode value
    # to the result and move towards right
    def inorderTraversalMorris(self, root):
        result = []
        curr = root
        while curr:
            if curr.left is None:
                result.append(curr.val)
                curr = curr.right
            else:
                leftChild = curr.left
                while leftChild.right and leftChild.right != curr:
                    leftChild = leftChild.right

                if leftChild.right is None:
                    # Make thread
                    # link leftChild.right to the curr
                    leftChild.right = curr
                    # explore the left side of the curr
                    curr = curr.left
                else:
                    # Thread exists; remove it and visit curr and go to the right
                    leftChild.right = None
                    result.append(curr.val)
                    curr = curr.right
        return result


"""
Normally, in inorder traversal (Left → Node → Right), 
we use a stack or recursion to remember how to get back up 
the tree after visiting the left child.

Morris traversal avoids this by:

Temporarily modifying the tree structure to create "threads" 
that let us return to parent nodes without needing extra memory.
"""


answer = Solution()
# root = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.left.right.left = TreeNode(6)
root.left.right.right = TreeNode(7)

root.right.left = TreeNode(9)
root.right.right = TreeNode(8)

print(answer.inorderTraversalRecursion(root))
print(answer.inorderTraversalStack(root))
print(answer.inorderTraversalMorris(root))
