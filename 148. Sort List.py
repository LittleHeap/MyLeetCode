# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        if not head:
            return None

        d = {}
        while head:
            d[head] = head.val
            head = head.next

        l = sorted(d.items(), key=lambda x: x[1])
        for i in range(len(l) - 1):
            l[i][0].next = l[i + 1][0]
        l[-1][0].next = None
        return l[0][0]