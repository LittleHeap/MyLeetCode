# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:

        res = [[float('inf'), None]]

        def deep(node, level):
            if not node:
                return [[None, None], None]
            else:
                l, ll = deep(node.left, level + 1)
                r, rr = deep(node.right, level + 1)
                if not l[0] and not r[0]:
                    if node.val == k:
                        res[0][0] = 0
                        res[0][1] = node.val
                        return [[1, node.val], level]
                    else:
                        return [[1, node.val], 0]
                elif l[0] and r[0]:
                    if node.val == k:
                        res[0] = min(res[0], min(l, r))
                        return [[min(l, r)[0] + 1, min(l, r)[1]], level]
                    elif ll:
                        res[0] = (res[0] if res[0][0] <= ll - level + r[0] else (ll - level + r[0], r[1]))
                        return [[min(l, r)[0] + 1, min(l, r)[1]], ll]
                    elif rr:
                        res[0] = (res[0] if res[0][0] <= rr - level + l[0] else (rr - level + l[0], l[1]))
                        return [[min(l, r)[0] + 1, min(l, r)[1]], rr]
                    else:
                        return [[min(l, r)[0] + 1, min(l, r)[1]], None]
                elif l[0]:
                    if node.val == k:
                        res[0] = min(res[0], l)
                        return [[l[0] + 1, l[1]], level]
                    else:
                        return [[l[0] + 1, l[1]], None]
                elif r[0]:
                    if node.val == k:
                        res[0] = min(res[0], r)
                        return [[r[0] + 1, r[1]], level]
                    else:
                        return [[r[0] + 1, r[1]], None]

        deep(root, 1)
        return res[0][1]