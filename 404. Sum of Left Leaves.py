# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        if not root:
            return 0

        res = [0]

        def deep(node, l, r):
            if not node.left and not node.right:
                if l:
                    res[0] += node.val
                return
            if node.left:
                deep(node.left, 1, 0)
            if node.right:
                deep(node.right, 0, 1)

        deep(root, 0, 0)
        return res[0]
