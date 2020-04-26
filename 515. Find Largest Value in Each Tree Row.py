# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:

        if not root:
            return []

        res = []

        q = [root]

        while q:
            newq = []
            cur = float('-inf')
            for node in q:
                cur = max(cur, node.val)
                if node.left:
                    newq.append(node.left)
                if node.right:
                    newq.append(node.right)
            res.append(cur)
            q = newq

        return res