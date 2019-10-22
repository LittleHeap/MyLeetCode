# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:

        if not root:
            return 0

        cur = [root]
        res = 0
        flag = 0
        while cur:
            newcur = []
            res += 1
            for ele in cur:
                if not ele.left and not ele.right:
                    flag = 1
                    break
                else:
                    if ele.left:
                        newcur.append(ele.left)
                    if ele.right:
                        newcur.append(ele.right)
            if flag == 1:
                break
            else:
                cur = newcur

        return res