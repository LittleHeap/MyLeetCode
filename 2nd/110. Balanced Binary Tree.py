# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        if not root:
            return 1

        def deep(node):
            if not node.left and not node.right:
                return 1
            else:
                l = 0
                r = 0
                if node.left:
                    l = deep(node.left)
                    if l == 0:
                        return 0
                if node.right:
                    r = deep(node.right)
                    if r == 0:
                        return 0
                if abs(r - l) > 1:
                    return 0
                else:
                    return max(r, l) + 1

        return deep(root)
