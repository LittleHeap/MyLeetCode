# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:

        def deep(node):
            if not node:
                return 0
            else:
                l = deep(node.left)
                r = deep(node.right)
                if l == 0 and r == 0:
                    return 1
                elif l == 0 and r != 0:
                    return r + 1
                elif r == 0 and l != 0:
                    return l + 1
                else:
                    return min(r, l) + 1

        return deep(root)