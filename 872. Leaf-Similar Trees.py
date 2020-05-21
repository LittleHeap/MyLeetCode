# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:

        def deep(node):
            if not node:
                return []
            else:
                l = deep(node.left)
                r = deep(node.right)
                if not l and not r:
                    return [node.val]
                else:
                    return l + r

        return deep(root1) == deep(root2)