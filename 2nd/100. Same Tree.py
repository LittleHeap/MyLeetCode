# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        res = set()

        def deep(node1, node2):
            if False in res:
                return
            if node1 is None:
                if node2 is not None:
                    res.add(False)
                return
            if node2 is None:
                if node1 is not None:
                    res.add(False)
                return
            deep(node1.left, node2.left)
            if node1.val != node2.val:
                res.add(False)
                return
            deep(node1.right, node2.right)

        deep(p, q)

        return not False in res