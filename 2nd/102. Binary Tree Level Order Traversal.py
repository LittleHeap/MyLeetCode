# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        cur = [root]

        res = []
        while cur:
            newcur = []
            rescur = []
            while cur:
                node = cur.pop(0)
                rescur.append(node.val)
                if node.left:
                    newcur.append(node.left)
                if node.right:
                    newcur.append(node.right)
            res.append(rescur)
            if not newcur:
                break
            else:
                cur = newcur

        return res
