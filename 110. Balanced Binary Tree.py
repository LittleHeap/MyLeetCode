# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        if not root:
            return True

        ans = set()

        def deep(node):
            if False in ans:
                return 0
            if not node.left and not node.right:
                return 1
            l, r = 0, 0
            if node.left:
                l = deep(node.left)
            if node.right:
                r = deep(node.right)
            if abs(l - r) >= 2:
                ans.add(False)
                return 0
            else:
                return max(l, r) + 1

        deep(root)

        return not False in ans
