"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':

        if not root:
            return None
        hold = []

        def mid(node):
            if node.left:
                mid(node.left)
            hold.append(node)
            if node.right:
                mid(node.right)

        mid(root)

        head = Node(hold[0].val)
        start = head

        for i in range(1, len(hold)):
            head.right = Node(hold[i].val)
            pre = head
            head = head.right
            head.left = pre

        head.right = start
        start.left = head

        return start