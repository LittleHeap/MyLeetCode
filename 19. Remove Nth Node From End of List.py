# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        start = head
        pre = None
        while head:
            head.next, pre, head = pre, head, head.next
        end = pre
        if n == 1:
            end = end.next
        else:
            for i in range(n - 2):
                pre = pre.next
            pre.next = pre.next.next
        p = None
        while end:
            end.next, p, end = p, end, end.next
        return p
