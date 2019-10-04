# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        if not root:
            return 0

        res = [0]

        def deep(node, level):
            if node is None:
                return

            res[0] = max(res[0], level)
            deep(node.left, level + 1)
            deep(node.right, level + 1)

        deep(root, 1)
        return res[0]