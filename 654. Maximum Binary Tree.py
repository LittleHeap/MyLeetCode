# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:

        def deep(cur):
            if not cur:
                return None
            else:
                i = cur.index(max(cur))
                node = TreeNode(cur[i])
                node.left = deep(cur[:i])
                node.right = deep(cur[i + 1:])
                return node

        return deep(nums)