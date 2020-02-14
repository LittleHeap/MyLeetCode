# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:

        res = [0]

        def deep(node):
            if not node:
                return None
            if not node.left and not node.right:
                res[0] = max(res[0], 1)
                return [1, node.val, node.val]
            else:
                l = deep(node.left)
                r = deep(node.right)
                if l == -1 or r == -1:
                    return -1
                if l is not None and r is not None:
                    if l[2] < node.val and r[1] > node.val:
                        res[0] = max(res[0], l[0] + r[0] + 1)
                        return [l[0] + r[0] + 1, l[1], r[2]]
                    else:
                        return -1
                elif l is None:
                    if r[1] > node.val:
                        res[0] = max(res[0], r[0] + 1)
                        return [r[0] + 1, node.val, r[2]]
                    else:
                        return -1
                elif r is None:
                    if l[2] < node.val:
                        res[0] = max(res[0], l[0] + 1)
                        return [l[0] + 1, l[1], node.val]
                    else:
                        return -1

        deep(root)
        return res[0]
