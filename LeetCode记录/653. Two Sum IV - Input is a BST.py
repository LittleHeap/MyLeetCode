# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        t = []

        def deep(node):
            if node is None:
                return
            t.append(node.val)
            deep(node.left)
            deep(node.right)

        deep(root)
        for i in range(len(t)):
            if k - t[i] in t[:i] or k - t[i] in t[i + 1:]:
                return True
        return False