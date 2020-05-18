# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: TreeNode) -> bool:

        d = defaultdict(int)

        def deep(node):
            if not node:
                return 0
            else:
                cur = deep(node.left) + node.val + deep(node.right)
                d[cur] += 1
                return cur

        sum = deep(root)

        return (sum / 2 in d if sum != 0 else d[sum] >= 2)