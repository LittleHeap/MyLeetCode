# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        node = []
        while head:
            node.append(head)
            head = head.next

        n = len(node)
        if n <= 1:
            return

        mid = n // 2
        l = 0
        r = n - 1
        while 1:
            node[l].next = node[r]
            l += 1
            node[r].next = node[l]
            r -= 1
            if r == mid or l == mid:
                node[mid].next = None
                break
