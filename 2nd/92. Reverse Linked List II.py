# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        if not head:
            return head
        if m == n:
            return head

        index = 1
        start = head
        pre = None
        lpre = None
        while head:
            if index == m:
                l = head
                lpre = pre
            elif index == n:
                r = head
                break
            pre = head
            head = head.next
            index += 1
        if lpre is not None:
            lpre.next = r
            pre = r.next
            while l != r:
                l.next, pre, l = pre, l, l.next
            l.next = pre
            return start
        else:
            start = r
            pre = r.next
            while l != r:
                l.next, pre, l = pre, l, l.next
            l.next = pre
            return start