# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        def deep(node):
            if node is None:
                return
            else:
                node.left, node.right = node.right, node.left
                deep(node.left)
                deep(node.right)

        deep(root)
        return root