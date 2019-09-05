# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        res = []

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        inorder(root)

        ans = float('inf')
        for i in range(len(res) - 1):
            ans = min(ans, abs(res[i] - res[i + 1]))

        return ans