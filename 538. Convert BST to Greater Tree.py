# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:

        def deep(node, val):
            if not node:
                return val
            else:
                val = deep(node.right, val)
                node.val += val
                return deep(node.left, node.val)

        deep(root, 0)
        return root