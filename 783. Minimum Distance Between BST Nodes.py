# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:

        self.res = float('inf')

        def deep(node):
            if not node.left and not node.right:
                return (node.val, node.val)
            elif node.left and node.right:
                lmin, lmax = deep(node.left)
                rmin, rmax = deep(node.right)
                self.res = min(self.res, node.val - lmax, rmin - node.val)
                return (lmin, rmax)
            elif node.left:
                lmin, lmax = deep(node.left)
                self.res = min(self.res, node.val - lmax)
                return (lmin, node.val)
            elif node.right:
                rmin, rmax = deep(node.right)
                self.res = min(self.res, rmin - node.val)
                return (node.val, rmax)

        deep(root)
        return self.res
