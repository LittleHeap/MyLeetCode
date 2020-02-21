# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        res = []

        def deep(node):
            if node is None:
                return 0
            if not node.left and not node.right:
                if len(res) < 1:
                    res.append([])
                res[0].append(node.val)
                return 1
            else:
                index = max(deep(node.left), deep(node.right))
                while len(res) < index + 1:
                    res.append([])
                res[index].append(node.val)
                return index + 1

        deep(root)
        return res