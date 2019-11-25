# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:

        if not root:
            return 0

        res = [0]

        def deep(node, n):
            res[0] = max(res[0], n)
            if node.left:
                if node.left.val == node.val + 1:
                    deep(node.left, n + 1)
                else:
                    deep(node.left, 1)
            if node.right:
                if node.right.val == node.val + 1:
                    deep(node.right, n + 1)
                else:
                    deep(node.right, 1)

        deep(root, 1)
        return res[0]