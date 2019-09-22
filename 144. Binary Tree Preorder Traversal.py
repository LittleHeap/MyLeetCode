# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        if not root:
            return []
        res = []

        def pre(node):
            if node is None:
                return
            res.append(node.val)
            pre(node.left)
            pre(node.right)

        pre(root)
        return res
