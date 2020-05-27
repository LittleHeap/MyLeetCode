# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:

        if not root:
            return True

        q = [(root, 1)]
        cur = 1
        while q:
            newq = []
            for i, (node, num) in enumerate(q):
                if (i != 0 and num != q[i - 1][1] + 1) or (i == 0 and num != cur):
                    return False
                if node.left:
                    newq.append((node.left, num * 2))
                if node.right:
                    newq.append((node.right, num * 2 + 1))
            if newq and len(q) != cur:
                return False
            q = newq
            cur *= 2

        return True