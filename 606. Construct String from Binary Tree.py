# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, t: TreeNode) -> str:

        if not t:
            return ''
        cur = str(t.val)
        left = self.tree2str(t.left)
        right = self.tree2str(t.right)
        if not left:
            if right:
                return cur + '()' + '(' + right + ')'
            else:
                return cur
        else:
            if right:
                return cur + '(' + left + ')' + '(' + right + ')'
            else:
                return cur + '(' + left + ')'