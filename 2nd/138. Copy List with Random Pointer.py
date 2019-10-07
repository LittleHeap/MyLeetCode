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

        nodes = []
        d = {}

        i = 0
        while head:
            nodes.append(head)
            d[head] = i
            i += 1
            head = head.next

        new = []
        for i in range(len(nodes)):
            newnode = Node(nodes[i].val, None, None)
            new.append(newnode)
            if i == 0:
                start = newnode
                pre = newnode
            else:
                pre.next = newnode
                pre = newnode

        cur = start
        for i in range(len(nodes)):
            if nodes[i].random is not None:
                index = d.get(nodes[i].random)
                new[i].random = new[index]
        return start
