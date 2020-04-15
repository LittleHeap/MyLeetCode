# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:

        def deep(cur):
            if not cur:
                return None
            elif len(cur) == 1:
                return TreeNode(post.pop())
            else:
                node = TreeNode(post.pop())
                index = cur.index(post[-1])
                node.right = deep(cur[index:])
                node.left = deep(cur[1:index])
                return node

        return deep(pre)