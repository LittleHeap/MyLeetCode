# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def deep(node, l):
            if len(l) == 0:
                return None
            node = TreeNode(max(l))
            index = l.index(node.val)
            leftl = l[:index]
            rightl = l[index + 1:]
            node.left = deep(node.left, leftl)
            node.right = deep(node.right, rightl)
            return node

        node = TreeNode(0)
        root = deep(node, nums)
        return root
