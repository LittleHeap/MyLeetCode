"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:

        if not root:
            return 0

        res = 0
        q = [root]

        while q:
            res += 1
            newq = []
            for node in q:
                for child in node.children:
                    newq.append(child)
            q = newq

        return res

