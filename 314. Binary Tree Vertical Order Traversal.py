# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:

        d = {}
        if not root:
            return []

        cur = [(root, 0)]
        while cur:
            newcur = []
            for ele in cur:
                if ele[1] not in d:
                    d[ele[1]] = [ele[0].val]
                else:
                    d[ele[1]].append(ele[0].val)
                if ele[0].left:
                    newcur.append((ele[0].left, ele[1] + 1))
                if ele[0].right:
                    newcur.append((ele[0].right, ele[1] - 1))
            cur = newcur

        res = d.items()
        temp = sorted(res, key=lambda x: x[0], reverse=True)
        ans = []
        for ele in temp:
            ans.append(ele[1])

        return ans