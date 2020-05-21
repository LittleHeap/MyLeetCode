# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: TreeNode, V: int) -> List[TreeNode]:

        self.big = None
        self.small = None

        def deep(node):
            if not node:
                return (None, None)
            else:
                if node.val > V:
                    if self.big is None:
                        self.big = node
                    big, small = deep(node.left)
                    node.left = big
                    return (node, small)
                else:
                    if self.small is None:
                        self.small = node
                    big, small = deep(node.right)
                    node.right = small
                    return (big, node)

        deep(root)
        return [self.small, self.big]
