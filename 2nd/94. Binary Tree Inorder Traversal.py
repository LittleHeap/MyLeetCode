# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        if not root:
            return root

        res = []

        def deep(node):
            if node is None:
                return
            deep(node.left)
            res.append(node.val)
            deep(node.right)

        deep(root)
        return res