"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':

        if node.right:
            cur = node.right
            while cur.left:
                cur = cur.left
            return cur
        elif node.parent:
            origin = node.val
            if node.parent.val > node.val:
                return node.parent
            else:
                while node.parent and node.parent.val < origin:
                    node = node.parent
                if node.parent:
                    return node.parent
                else:
                    return None
        else:
            return None



