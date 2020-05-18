# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:

        s = set()

        def deep(node):
            if not node:
                return False
            else:
                if k - node.val in s:
                    return True
                else:
                    s.add(node.val)
                    return deep(node.left) or deep(node.right)

        return deep(root)