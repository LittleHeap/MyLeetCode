# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:

        res = [None, float('inf')]

        def deep(node):
            if not node:
                return
            dis = abs(node.val - target)
            if dis < res[1]:
                res[0] = node.val
                res[1] = dis
            if node.val == target:
                return
            elif node.val > target:
                deep(node.left)
            else:
                deep(node.right)

        deep(root)
        return res[0]