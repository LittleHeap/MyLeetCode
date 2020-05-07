# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:

        res = [0]

        def deep(node):
            if not node:
                return 0
            else:
                l = deep(node.left)
                r = deep(node.right)
                res[0] += abs(l - r)
                return l + r + node.val

        deep(root)
        return res[0]