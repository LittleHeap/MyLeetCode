# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        if not root:
            return True

        res1 = []
        res2 = []

        def pre(node):
            if node is None:
                res1.append('1')
            else:
                res1.append(node.val)
                pre(node.left)
                pre(node.right)

        pre(root)

        def back(node):
            if node is None:
                res2.append('1')
            else:
                res2.append(node.val)
                back(node.right)
                back(node.left)

        back(root)

        return res1 == res2