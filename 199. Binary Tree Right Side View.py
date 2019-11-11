# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:

        if not root:
            return []
        res = []
        cur = [root]
        while cur:
            res.append(cur[-1].val)
            newcur = []
            for node in cur:
                if node.left:
                    newcur.append(node.left)
                if node.right:
                    newcur.append(node.right)
            cur = newcur

        return res