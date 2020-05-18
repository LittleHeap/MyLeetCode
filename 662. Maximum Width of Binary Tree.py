# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:

        if not root:
            return 0

        q = [[1, root]]

        res = 0
        while q:
            newq = []
            res = max(res, q[-1][0] - q[0][0] + 1)
            for (index, node) in q:
                if node.left:
                    newq.append((2 * index, node.left))
                if node.right:
                    newq.append((2 * index + 1, node.right))
            q = newq
        return res