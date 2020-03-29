# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:

        res = []

        def deep(node, cur, l):
            if not node:
                return
            else:
                cur -= node.val
                newl = l.copy()
                newl.append(node.val)
                if cur == 0 and not node.left and not node.right:
                    res.append(newl)
                    return
                else:
                    deep(node.left, cur, newl)
                    deep(node.right, cur, newl)

        deep(root, sum, [])

        return res