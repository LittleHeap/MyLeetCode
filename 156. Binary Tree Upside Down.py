# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        def deep(node, lr):
            if not node.left and not node.right:
                return node

            l, r = None, None
            if node.left:
                l = deep(node.left, 0)
            if node.right:
                r = deep(node.right, 1)

            if lr:
                return node
            else:
                cur = l
                while cur.right:
                    cur = cur.right
                cur.right = TreeNode(node.val)
                cur.left = r
                return l

        return deep(root, 0)