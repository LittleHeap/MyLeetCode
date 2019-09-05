# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        X = []
        Y = []

        def deep(node, level, f):
            if node is None:
                return
            if node.val == x:
                X.append(level)
                X.append(f)
            elif node.val == y:
                Y.append(level)
                Y.append(f)
            deep(node.left, level + 1, node)
            deep(node.right, level + 1, node)

        deep(root, 0, None)
        if X[0] == Y[0] and X[1] != Y[1]:
            return True
        else:
            return False