# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def func(l):
            if not l:
                return None
            node = TreeNode(postorder.pop())
            index = l.index(node.val)
            node.right = func(l[index + 1:])
            node.left = func(l[:index])
            return node

        return func(inorder)