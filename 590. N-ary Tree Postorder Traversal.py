"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        if not root:
            return []
        else:
            cur = []
            for child in root.children:
                cur += self.postorder(child)
            cur += [root.val]
            return cur