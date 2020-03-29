# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def deep(node):
            if not node:
                return None
            elif not node.left and not node.right:
                return node
            else:
                l = deep(node.left)
                r = deep(node.right)
                if l and r:
                    node.left = None
                    node.right = l
                    temp = l
                    while temp.right:
                        temp = temp.right
                    temp.right = r
                    return node
                elif l and not r:
                    node.left = None
                    node.right = l
                    return node
                elif not l and r:
                    return node

        return deep(root)