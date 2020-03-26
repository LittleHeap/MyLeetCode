# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def deep(cur):
            if not cur:
                return None
            node = TreeNode(preorder.pop(0))
            index = cur.index(node.val)
            node.left = deep(cur[:index])
            node.right = deep(cur[index + 1:])
            return node

        return deep(inorder)