# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:

        if not root:
            return []

        q = [root]

        res = []
        while q:
            cur = 0
            newq = []
            for ele in q:
                cur += ele.val
                if ele.left:
                    newq.append(ele.left)
                if ele.right:
                    newq.append(ele.right)
            res.append(cur / len(q))
            q = newq

        return res