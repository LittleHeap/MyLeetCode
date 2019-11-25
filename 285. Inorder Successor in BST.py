# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':

        res = []

        if not root:
            return None

        def deep(node):
            if not node:
                return
            deep(node.left)
            res.append(node)
            deep(node.right)

        deep(root)

        n = len(res)
        for i in range(n):
            if res[i] == p:
                if i + 1 < n:
                    return res[i + 1]
                else:
                    return None