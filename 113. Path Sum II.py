# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:

        if not root:
            return []

        res = []

        def deep(node, s, cur):
            s += node.val
            newcur = cur.copy()
            newcur.append(node.val)
            if not node.left and not node.right:
                if s == sum:
                    res.append(newcur)
                return
            if node.left:
                deep(node.left, s, newcur)
            if node.right:
                deep(node.right, s, newcur)

        deep(root, 0, [])
        return res
