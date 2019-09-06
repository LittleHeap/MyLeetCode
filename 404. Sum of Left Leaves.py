# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        ans = [0]

        def deep(node, left):
            if node is None:
                return

            if not node.left and not node.right:
                if left:
                    ans[0] += node.val
                    return
                else:
                    return

            deep(node.left, 1)
            deep(node.right, 0)

        deep(root, 0)
        return ans[0]
