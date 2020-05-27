# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        q = [(root, 1)]

        while q:
            newq = []
            xnum, ynum = 0, 0
            for i, (node, num) in enumerate(q):
                if node.val == x:
                    xnum = num
                if node.val == y:
                    ynum = num
                newq += ([(node.left, num * 2)] if node.left else [])
                newq += ([(node.right, num * 2 + 1)] if node.right else [])
            if xnum and ynum and (xnum // 2 != ynum // 2):
                return True
            elif xnum or ynum:
                return False
            else:
                q = newq