# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:

        if not root:
            return 0

        cur = [root]

        ans = 0
        while cur:
            newcur = []
            while cur:
                node = cur.pop()
                ans += 1
                if node.left:
                    newcur.append(node.left)
                if node.right:
                    newcur.append(node.right)
            cur = newcur

        return ans