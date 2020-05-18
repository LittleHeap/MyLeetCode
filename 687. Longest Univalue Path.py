# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:

        res = [0]

        def deep(node):
            if not node:
                return (None, 0)
            else:
                l, ll = deep(node.left)
                r, rr = deep(node.right)
                if l == node.val and r == node.val:
                    res[0] = max(res[0], ll + rr + 2)
                    return (node.val, max(ll, rr) + 1)
                elif l == node.val:
                    res[0] = max(res[0], ll + 1)
                    return (node.val, ll + 1)
                elif r == node.val:
                    res[0] = max(res[0], rr + 1)
                    return (node.val, rr + 1)
                else:
                    return (node.val, 0)

        deep(root)
        return res[0]