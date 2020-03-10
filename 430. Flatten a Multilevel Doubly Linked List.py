"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Node') -> 'Node':

        if not head:
            return head

        res = []

        def dfs(node):
            if node is None:
                return None
            res.append(node.val)
            if node.child:
                temp = node.next
                node.next = node.child
                node.child.prev = node
                node.child = None
                last = dfs(node.next)
                if last:
                    last.next = temp
                if temp:
                    temp.prev = last
                return dfs(temp)
            elif node.next:
                return dfs(node.next)
            else:
                return node

        dfs(head)

        return head