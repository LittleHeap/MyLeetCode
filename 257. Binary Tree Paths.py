# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        res = []

        def deep(node, cur):
            if not node:
                return
            if not node.left and not node.right:
                newcur = cur.copy()
                newcur.append(node.val)
                ans = ''
                for ele in newcur:
                    ans = ans + str(ele) + '->'
                ans = ans[:-2]
                res.append(ans)
                return
            else:
                newcur = cur.copy()
                newcur.append(node.val)
                deep(node.left, newcur)
                deep(node.right, newcur)

        deep(root, [])
        return res