# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:

        if not root:
            return 0

        res = [0]

        def deep(node, cur):
            cur.append(node.val)
            if not node.left and not node.right:
                s = ''
                for ele in cur:
                    s += str(ele)
                s = int(s)
                res[0] += s
                return
            if node.left:
                newcur = cur.copy()
                deep(node.left, newcur)
            if node.right:
                newcur = cur.copy()
                deep(node.right, newcur)

        deep(root, [])
        return res[0]
