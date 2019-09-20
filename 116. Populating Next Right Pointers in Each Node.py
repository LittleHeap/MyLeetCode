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

        root.next = None
        cur = [root]

        while cur:
            newcur = []
            if cur[0].left is not None:
                for node in cur:
                    newcur.append(node.left)
                    newcur.append(node.right)
                newcur.append(None)
                for i in range(len(newcur) - 1):
                    newcur[i].next = newcur[i + 1]
                newcur.pop()
                cur = newcur
            else:
                break
        return root
