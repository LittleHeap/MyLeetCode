# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ''
        res = []

        def indeep(node, cur):
            if node is None:
                return
            cur += str(node.val)
            if node.left:
                cur += indeep(node.left, '')
            if not node.left and node.right:
                cur += '()'
                cur += indeep(node.right, '')
            elif node.right:
                cur += indeep(node.right, '')
            return '(' + cur + ')'

        return indeep(t, '')[1:-1]
