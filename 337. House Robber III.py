# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:

        def deep(node):
            if not node:
                return [0, 0]
            else:
                left = deep(node.left)
                right = deep(node.right)
                return [node.val + left[1] + right[1], max(left) + max(right)]

        return max(deep(root))
