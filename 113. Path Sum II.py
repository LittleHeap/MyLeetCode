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

        def deep(node, target, cur):
            if not node:
                return
            cur.append(node.val)
            if not node.left and not node.right:
                if target - node.val == 0:
                    res.append(cur)
                    return
                else:
                    return
            newcur = cur.copy()
            newtarget = target - node.val
            deep(node.left, newtarget, newcur)
            newcur = cur.copy()
            newtarget = target - node.val
            deep(node.right, newtarget, newcur)

        deep(root, sum, [])
        return res
