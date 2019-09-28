# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return []

        cur = [root]
        while cur:
            res.append(cur[-1].val)
            newcur = []
            while cur:
                node = cur.pop(0)
                if node.left:
                    newcur.append(node.left)
                if node.right:
                    newcur.append(node.right)
            cur = newcur

        return res
