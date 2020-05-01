# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> TreeNode:

        if not s:
            return None

        def deep(cur):
            if not cur:
                return None
            elif not '(' in cur:
                return TreeNode(int(cur))
            else:
                index = cur.index('(')
                node = TreeNode(int(cur[:index]))
                cur = cur[index:]
                l, r = 0, 0
                index = 0
                for i, char in enumerate(cur):
                    if char == '(':
                        l += 1
                    if char == ')':
                        r += 1
                    if l == r:
                        index = i
                        break
                node.left = deep(cur[1:index])
                node.right = deep(cur[index + 2:-1])
            return node

        return deep(s)