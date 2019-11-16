# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def deep(node):
            if p.val == q.val and p.val == node.val:
                return node
            else:
                if p.val < node.val and q.val < node.val:
                    return deep(node.left)
                elif p.val > node.val and q.val > node.val:
                    return deep(node.right)
                else:
                    return node

        return deep(root)