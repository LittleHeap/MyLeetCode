# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        if not preorder:
            return None

        root = TreeNode(preorder[0])

        def deep(fa, l, left):
            if not l:
                return
            if fa is None:
                index = l.index(root.val)
                preorder.pop(0)
                deep(root, l[:index], 1)
                deep(root, l[index + 1:], 0)
            else:
                node = TreeNode(preorder.pop(0))
                index = l.index(node.val)
                if left:
                    fa.left = node
                else:
                    fa.right = node
                deep(node, l[:index], 1)
                deep(node, l[index + 1:], 0)

        deep(None, inorder, None)
        return root