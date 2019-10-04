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

        cur = [root]

        while cur:
            cur.append(None)
            for i in range(len(cur) - 1):
                cur[i].next = cur[i + 1]
            cur.pop()
            newcur = []
            for node in cur:
                if node.left:
                    newcur.append(node.left)
                if node.right:
                    newcur.append(node.right)
            if not newcur:
                break
            else:
                cur = newcur

        return root
