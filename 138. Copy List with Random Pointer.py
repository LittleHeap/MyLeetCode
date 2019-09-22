"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        if not head:
            return head

        oristart = head
        ori = []
        orid = {}
        index = 0
        res = []

        resstart = Node(head.val, None, None)
        pre = resstart
        while head:
            ori.append(head)
            orid[head] = index
            index += 1
            node = Node(head.val, None, None)
            res.append(node)
            pre.next = node
            pre = node
            head = head.next

        resstart = resstart.next
        ans = resstart
        while oristart:
            if oristart.random:
                index = orid.get(oristart.random)
                resstart.random = res[index]
            oristart = oristart.next
            resstart = resstart.next

        return ans
