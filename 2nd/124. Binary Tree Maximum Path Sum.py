# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:

        res = [float('-inf')]

        def deep(node):

            nodeval = node.val
            if not node.left and not node.right:
                return nodeval

            if node.left:
                nodeleft = deep(node.left)
                res[0] = max(res[0], nodeleft)
            if node.right:
                noderight = deep(node.right)
                res[0] = max(res[0], noderight)

            if node.left and not node.right:
                return max(nodeval, nodeval + nodeleft)
            elif node.right and not node.left:
                return max(nodeval, nodeval + noderight)
            else:
                res[0] = max(res[0], nodeval + nodeleft + noderight)
                return max(nodeval, nodeval + noderight, nodeval + nodeleft)

        ans = deep(root)
        return max(res[0], ans)