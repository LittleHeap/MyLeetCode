# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:

        res = []

        def deep(remain):
            if remain == 1:
                return [TreeNode(0)]
            remain -= 1
            cur = []
            for i in range(1, remain, 2):
                left = deep(i)
                right = deep(remain - i)
                for l in left:
                    for r in right:
                        node = TreeNode(0)
                        node.left = l
                        node.right = r
                        cur.append(node)
            return cur

        return deep(N)