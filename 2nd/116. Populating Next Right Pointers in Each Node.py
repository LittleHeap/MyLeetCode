"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return

        q = [root]

        while q:
            newq = []
            for node in q:
                if node.left:
                    newq.append(node.left)
                if node.right:
                    newq.append(node.right)
            for i in range(len(newq) - 1):
                newq[i].next = newq[i + 1]
            q = newq

        return root