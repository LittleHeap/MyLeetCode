# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        res = []

        def inorder(node):
            if not node:
                return
            else:
                inorder(node.left)
                res.append(node.val)
                inorder(node.right)

        inorder(root)
        temp = res.copy()
        temp.sort()
        p = []
        for i in range(len(res)):
            if res[i] != temp[i]:
                p.append(res[i])

        def deep(node):
            if not node:
                return
            else:
                if node.val == p[0]:
                    node.val = p[1]
                elif node.val == p[1]:
                    node.val = p[0]
                deep(node.left)
                deep(node.right)

        deep(root)
        return root
