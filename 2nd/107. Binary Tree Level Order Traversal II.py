# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        cur = [root]

        res = []

        while cur:
            newcur = []
            temp = []
            for ele in cur:
                temp.append(ele.val)
            res.insert(0, temp)
            while cur:
                node = cur.pop(0)
                if node.left:
                    newcur.append(node.left)
                if node.right:
                    newcur.append(node.right)
            cur = newcur

        return res