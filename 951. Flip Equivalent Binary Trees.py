# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:

        def deep(node1, node2):
            if not node1 and not node2:
                return 1
            elif node1 and node2:
                if node1.val != node2.val:
                    return 0
                a = deep(node1.left, node2.left)
                b = deep(node1.right, node2.right)
                c = deep(node1.left, node2.right)
                d = deep(node1.right, node2.left)
                if (a == 1 and b == 1) or (c == 1 and d == 1):
                    return 1
                else:
                    return 0
            else:
                return 0

        return deep(root1, root2)