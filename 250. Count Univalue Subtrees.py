# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:

        res = [0]

        def deep(node):
            if not node:
                return set()
            else:
                cur = set()
                cur.add(node.val)
                cur = cur | deep(node.left)
                cur = cur | deep(node.right)
                if len(cur) == 1:
                    res[0] += 1
                return cur

        deep(root)
        return res[0]