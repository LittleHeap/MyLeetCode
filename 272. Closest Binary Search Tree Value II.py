import heapq


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:

        res = []

        def deep(node):
            if not node:
                return
            dis = abs(node.val - target)
            heapq.heappush(res, (dis, node.val))
            deep(node.left)
            deep(node.right)

        deep(root)
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(res)[1])
        return ans