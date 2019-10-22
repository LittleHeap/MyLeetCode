# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        if not root:
            return False

        find = [0]

        def deep(node, s):
            if find[0] == 1:
                return
            s += node.val
            if not node.left and not node.right:
                if s == sum:
                    find[0] = 1
                return
            if node.left:
                deep(node.left, s)
            if node.right:
                deep(node.right, s)

        deep(root, 0)
        return find[0] == 1