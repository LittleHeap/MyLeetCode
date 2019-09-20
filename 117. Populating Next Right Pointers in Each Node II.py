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
            return None

        root.next = None
        cur = [root]

        while cur:
            n = []
            for node in cur:
                if node.left:
                    n.append(node.left)
                if node.right:
                    n.append(node.right)
            if not n:
                break
            n.append(None)
            for i in range(len(n) - 1):
                n[i].next = n[i + 1]
            n.pop()
            cur = n

        return root