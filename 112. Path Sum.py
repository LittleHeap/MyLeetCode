# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        if not root:
            return False

        def deep(node):
            if not node.left and not node.right:
                return [node.val]
            l, r = [], []
            if node.left:
                l = deep(node.left)
            if node.right:
                r = deep(node.right)
            l.extend(r)
            for i in range(len(l)):
                l[i] += node.val
            return l

        res = deep(root)
        if sum in res:
            return True
        else:
            return False
