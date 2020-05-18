# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:

        d = defaultdict(list)

        def deep(node):
            if not node:
                return [None]
            else:
                cur = deep(node.left) + deep(node.right) + [node.val]
                d[tuple(cur)].append(node)
                return cur

        deep(root)

        return [d[ele][0] for ele in d if len(d[ele]) > 1]


