# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def deep(node):
            if not node:
                return None
            if not node.left and not node.right:
                return node
            if node.left:
                temp = node.right
                node.right = deep(node.left)
                node.left = None
                cur = node.right
                while cur.right:
                    cur = cur.right
                cur.right = deep(temp)
            else:
                node.right = deep(node.right)
            return node

        if root:
            deep(root)
