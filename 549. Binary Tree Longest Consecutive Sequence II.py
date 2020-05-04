# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:

        res = [0]

        def deep(node):
            if not node:
                return (0, 0)
            else:
                inc, dec = 1, 1
                l_up, l_down = deep(node.left)
                r_up, r_down = deep(node.right)
                if node.left:
                    if node.val == node.left.val + 1:
                        inc = max(inc, l_up + 1)
                    if node.val == node.left.val - 1:
                        dec = max(dec, l_down + 1)
                if node.right:
                    if node.val == node.right.val + 1:
                        inc = max(inc, r_up + 1)
                    if node.val == node.right.val - 1:
                        dec = max(dec, r_down + 1)
                res[0] = max(res[0], inc + dec - 1)
                return (inc, dec)

        deep(root)
        return res[0]


