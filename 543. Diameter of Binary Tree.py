# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        res = [0]

        def deep(node):
            if not node:
                return 0
            else:
                l = deep(node.left)
                r = deep(node.right)
                res[0] = max(res[0], l + r)
                return max(l + 1, r + 1)

        deep(root)
        return res[0]