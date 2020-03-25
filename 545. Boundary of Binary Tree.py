# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        l = []

        def left(node):
            if node.left:
                l.append(node.left.val)
                node = node.left
                left(node)
            elif not node.left and node.right:
                l.append(node.right.val)
                node = node.right
                left(node)

        if root.left:
            left(root)

        r = []

        def right(node):
            if node.right:
                r.append(node.right.val)
                node = node.right
                right(node)
            elif not node.right and node.left:
                r.append(node.left.val)
                node = node.left
                right(node)

        if root.right:
            right(root)

        b = []

        def bottom(node):
            if not node:
                return
            if not node.left and not node.right:
                b.append(node.val)
            else:
                bottom(node.left)
                bottom(node.right)

        if root.left or root.right:
            bottom(root)

        r.reverse()
        res = [root.val] + l[:-1] + b + r[1:]

        return res









