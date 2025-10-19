class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    # TC = O(n)
    # SC = O(n)
    def postorderRecursive(self, root):
        result = []

        def postorder(root):
            if root is None:
                return []
            postorder(root.left)
            postorder(root.right)
            result.append(root.val)

        postorder(root)
        return result

    """
    Post order is  Left -> Right -> Root
    Reverse of it is ==> Root -> Right -> Left
    1. We initially push the root node at the beginning
    2. While stack1 is not empty we keeping popping node and push it to stack 2
    While we pop the node, we check if it has a left child and right child.
    If Yes, then we append left and right child nodes onto the stack 1
    3. We pop all the nodes from stack2 and append the values to the result array
    """

    def postorderUsingTwoStack(self, root):
        if root is None:
            return []
        stack1 = [root]
        stack2 = []
        result = []
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)

        while stack2:
            node = stack2.pop()
            result.append(node.val)
        return result

    """
    1. We traverse as far left as possible, pushing nodes onto the stack.

    2. When we reach a node with no left child:
    i.) If it has a right child that has not been processed, we move to the right.

    ii.), it means both left and right are processed,
        so we process the node (i.e., add its value to the result).

    3. We track the last node we processed using prev.

    ✅ With curr = None

    After processing, we stop going down left.
    Control returns to the top of the stack.
    Correct postorder traversal.

    With curr = None, we force the traversal to not go down the left path again,
    and instead continue unwinding the stack.

    ❌ Without curr = None

    After processing a node, curr is still pointing to it.
    while curr: is true → goes left again → infinite loop or reprocess
    You might see duplicates or wrong output.
    """

    # TC = O(n)
    # SC = O(n)
    def postorderOneStack(self, root):
        if root is None:
            return []
        curr = root
        stack = []
        result = []
        prev = None  # (previously visited node) pointer to help us decide when to process a node.
        while curr or stack:
            # Go far left as possible
            while curr:
                stack.append(curr)
                curr = curr.left

            # peek at the top of the stack
            node = stack[-1]

            # If right node exists and unprocessed, then move to the right node
            if node.right and node.right != prev:
                curr = node.right
            # Process the node
            else:
                stack.pop()
                result.append(node.val)
                prev = node  # Mark this node as processed
                curr = None  # Prevent going left again
        return result


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

print(answer.postorderRecursive(root))
print(answer.postorderUsingTwoStack(root))
print(answer.postorderOneStack(root))
