"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        if not root:
            return []

        res = []

        q = [root]

        while q:
            cur = []
            newq = []
            for ele in q:
                cur.append(ele.val)
                for c in ele.children:
                    newq.append(c)
            q = newq
            res.append(cur)

        return res