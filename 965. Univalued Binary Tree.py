# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:

        self.val = root.val

        q = [root]
        while q:
            cur = q.pop(0)
            if cur.val != self.val:
                return False
            else:
                q += ([cur.left] if cur.left else [])
                q += ([cur.right] if cur.right else [])

        return True