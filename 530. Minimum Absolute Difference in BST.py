# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:

        hold = []

        def deep(node):
            if not node:
                return
            else:
                hold.append(node.val)
                deep(node.left)
                deep(node.right)

        deep(root)

        hold.sort()
        res = float('inf')
        for i in range(1, len(hold)):
            res = min(hold[i] - hold[i - 1], res)

        return res