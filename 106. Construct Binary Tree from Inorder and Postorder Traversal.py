# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def deep(inor):
            if not inor:
                return None
            node = TreeNode(postorder.pop())
            index = inor.index(node.val)
            node.right = deep(inor[index + 1:])
            node.left = deep(inor[:index])
            return node

        return deep(inorder)