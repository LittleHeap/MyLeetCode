# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res = []

        def deep(node):
            if not node:
                return
            deep(node.left)
            res.append(node.val)
            deep(node.right)

        deep(root)
        return res[k - 1]