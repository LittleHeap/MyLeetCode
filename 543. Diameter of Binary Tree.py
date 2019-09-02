# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        if not root:
            return 0

        def deep(node, level):
            if not node.left and not node.right:
                return level
            l, r = 0, 0
            if node.left:
                l = deep(node.left, level + 1)
            if node.right:
                r = deep(node.right, level + 1)
            res.append(l + r - level * 2)
            return max(l, r)

        deep(root, 0)
        return max(res)
