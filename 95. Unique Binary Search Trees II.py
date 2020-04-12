# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        if n == 0:
            return []
        res = []

        def deep(remain):
            if not remain:
                return [None]
            else:
                cur = []
                for i, ele in enumerate(remain):
                    l = deep(remain[:i])
                    r = deep(remain[i + 1:])
                    for left in l:
                        for right in r:
                            node = TreeNode(ele)
                            node.left = left
                            node.right = right
                            cur.append(node)
                return cur

        return deep([i for i in range(1, n + 1)])


