# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        res = [0]

        def deep(node):
            if res[0] == 1:
                return
            if not node:
                return 0
            left = deep(node.left)
            right = deep(node.right)
            if res[0] == 1:
                return
            if abs(left - right) >= 2:
                res[0] = 1
            return max(left, right) + 1

        deep(root)
        return res[0] == 0