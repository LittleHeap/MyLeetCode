# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:

        def deep(node):
            if not node:
                return 0
            else:
                l = deep(node.left)
                r = deep(node.right)
                node.left = (None if not l else node.left)
                node.right = (None if not r else node.right)
                return l + r + node.val

        res = deep(root)
        return (root if res else None)