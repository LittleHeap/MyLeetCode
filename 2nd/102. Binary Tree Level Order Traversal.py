# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        q = []
        cur = []

        res = []

        q.append(root)
        cur.append(root.val)

        while q:
            res.append(cur)
            newq = []
            newcur = []
            while q:
                node = q.pop(0)
                if node.left:
                    newq.append(node.left)
                    newcur.append(node.left.val)
                if node.right:
                    newq.append(node.right)
                    newcur.append(node.right.val)
            q = newq
            cur = newcur

        return res