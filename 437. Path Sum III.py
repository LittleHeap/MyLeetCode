# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:

        res = [0]

        def deep(node, cur):
            if not node:
                return
            if node.val in cur:
                res[0] += cur.get(node.val)
            if node.val == sum:
                res[0] += 1
            newcur = {}
            for ele in cur:
                newcur[ele - node.val] = cur.get(ele)
            newcur[sum - node.val] = newcur.get(sum - node.val, 0) + 1
            deep(node.left, newcur)
            deep(node.right, newcur)

        deep(root, {})
        return res[0]