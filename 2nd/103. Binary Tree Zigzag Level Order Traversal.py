# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        res = []
        cur = [root]
        flag = 0
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
            if flag:
                rescur.reverse()
                res.append(rescur)
            else:
                res.append(rescur)
            flag = 1 - flag
            if not newcur:
                break
            else:
                cur = newcur

        return res
