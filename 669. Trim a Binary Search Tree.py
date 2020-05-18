# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:

        def deep(node, L, R):
            if not node:
                return None
            else:
                if node.val >= L and node.val <= R:
                    node.left = deep(node.left, L, R)
                    node.right = deep(node.right, L, R)
                    return node
                elif node.val < L:
                    return deep(node.right, L, R)
                elif node.val > R:
                    return deep(node.left, L, R)

        return deep(root, L, R)