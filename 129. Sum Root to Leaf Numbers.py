# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:

        if not root:
            return 0

        def deep(node, cur):
            if not node:
                return 0
            newcur = cur.copy()
            newcur.append(str(node.val))
            if not node.left and not node.right:
                return int(''.join(newcur))
            return deep(node.left, newcur) + deep(node.right, newcur)

        return deep(root, [])
