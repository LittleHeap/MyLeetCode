# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:

        if not root:
            return []

        def deep(node, d):
            if not node:
                return
            else:
                deep(node.left, d)
                deep(node.right, d)
                d[node.val] = d.get(node.val, 0) + 1

        d = {}
        deep(root, d)
        # print(d)

        res = []
        cur = sorted(d.items(), key=lambda x: x[1])[-1][1]
        for key in list(d.keys()):
            if d[key] == cur:
                res.append(key)

        return res