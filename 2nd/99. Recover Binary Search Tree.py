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
        if not root:
            return root
        res = []

        def deep(node):
            if node is None:
                return
            else:
                deep(node.left)
                res.append(node.val)
                deep(node.right)

        deep(root)

        other = res.copy()
        other.sort()
        d = {}
        for i in range(len(res)):
            if res[i] != other[i]:
                d[res[i]] = other[i]
                d[other[i]] = res[i]
                break
        fin = set()

        def deep(node):
            if True in fin:
                return
            if node is None:
                return
            else:
                deep(node.left)
                if node.val in d:
                    temp = node.val
                    node.val = d[node.val]
                    d.pop(temp)
                    if len(d) == 0:
                        fin.add(True)
                deep(node.right)

        deep(root)
