# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:

        if not root:
            return -1

        q = []
        q.append(root)
        _min = root.val
        sec = float('inf')

        while q:
            cur = q.pop(0)
            if cur.val > _min:
                sec = min(sec, cur.val)
            else:
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

        return -1 if sec == float('inf') else sec