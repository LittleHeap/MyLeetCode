# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        self.find = 0

        def deep(node, cur):
            if not node or self.find:
                return
            else:
                cur -= node.val
                if cur == 0 and not node.left and not node.right:
                    self.find = 1
                    return
                deep(node.left, cur)
                deep(node.right, cur)

        deep(root, sum)

        return self.find