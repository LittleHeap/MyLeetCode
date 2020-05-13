# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:

        if d == 1:
            node = TreeNode(val=v, left=root)
            return node

        q = [root]
        while d - 2:
            newq = []
            for node in q:
                if node.left:
                    newq.append(node.left)
                if node.right:
                    newq.append(node.right)
            q = newq
            d -= 1

        for node in q:
            l = node.left
            r = node.right
            node.left = TreeNode(v)
            node.right = TreeNode(v)
            node.left.left = l
            node.right.right = r

        return root