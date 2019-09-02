# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        res = set()

        def deep(node):
            if node is None:
                return
            res.add(node.val)
            deep(node.left)
            deep(node.right)

        deep(root)
        if len(res) == 1:
            return True
        else:
            return False
