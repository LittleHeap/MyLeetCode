# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:

        if not root:
            return []

        d = defaultdict(int)

        def deep(node):
            if not node:
                return 0
            else:
                cur = deep(node.left) + deep(node.right) + node.val
                d[cur] += 1
                return cur

        deep(root)

        most = max(d.items(), key=lambda x: x[1])[1]

        return [ele[0] for ele in d.items() if ele[1] == most]

