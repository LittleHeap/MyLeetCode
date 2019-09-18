# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        res = []
        curnode = []
        curnum = []
        flag = 0

        curnum.append(root.val)
        res.append(curnum)
        curnode = []
        if root.left:
            curnode.append(root.left)
        if root.right:
            curnode.append(root.right)
        flag = 1

        while curnode:
            curnum = []
            temp = []
            while curnode:
                node = curnode.pop(0)
                curnum.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            if flag:
                curnum.reverse()
                res.append(curnum)
                flag = 0
            else:
                res.append(curnum)
                flag = 1
            curnode = temp

        return res
