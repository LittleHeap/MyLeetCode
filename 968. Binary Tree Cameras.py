# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:

        def deep(node):
            if not node.left and not node.right:
                return (0, 0, 0)
            elif node.left and node.right:
                l, lnum, lc = deep(node.left)
                r, rnum, rc = deep(node.right)
                if not l or not r:
                    return (1, lnum + rnum + 1, 1)
                else:
                    if lc or rc:
                        return (1, lnum + rnum, 0)
                    else:
                        return (0, lnum + rnum, 0)
            elif node.left:
                l, lnum, lc = deep(node.left)
                if not l:
                    return (1, lnum + 1, 1)
                else:
                    if lc:
                        return (1, lnum, 0)
                    else:
                        return (0, lnum, 0)
            elif node.right:
                r, rnum, rc = deep(node.right)
                if not r:
                    return (1, rnum + 1, 1)
                else:
                    if rc:
                        return (1, rnum, 0)
                    else:
                        return (0, rnum, 0)

        mid, num, c = deep(root)
        if not mid:
            return num + 1
        else:
            return num
