# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        if not inorder:
            return None

        def deep(i, j):
            if i == j:
                return None
            if j - i == 1:
                return TreeNode(postorder.pop())
            node = TreeNode(postorder.pop())
            index = inorder.index(node.val)
            lstart = i
            lend = index
            rstart = index + 1
            rend = j
            node.right = deep(rstart, rend)
            node.left = deep(lstart, lend)
            return node

        return deep(0, len(inorder))
