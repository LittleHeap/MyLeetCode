# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        if not root:
            return True

        def pre(node, cur):
            if not node:
                cur.append(None)
            else:
                cur.append(node.val)
                pre(node.left, cur)
                pre(node.right, cur)

        def back(node, cur):
            if not node:
                cur.append(None)
            else:
                cur.append(node.val)
                back(node.right, cur)
                back(node.left, cur)

        l = []
        r = []

        pre(root, l)
        back(root, r)

        return l == r
