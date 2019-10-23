"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return root

        l = [root]

        while l:
            nl = []
            n = len(l)
            for i in range(len(l)):
                if l[i].left:
                    nl.append(l[i].left)
                if l[i].right:
                    nl.append(l[i].right)
                if i == n - 1:
                    break
                l[i].next = l[i + 1]
            l = nl

        return root
