# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n or not head:
            return head

        l = None
        r = None
        lpre = None
        index = 0
        pre = None
        start = head

        while head:
            index += 1
            if index == m:
                l = head
                lpre = pre
            if index == n:
                r = head
                break
            pre = head
            head = head.next

        if m != 1:
            lpre.next = r
        pre = None
        cur = l
        while cur != r:
            cur.next, pre, cur = pre, cur, cur.next
        l.next = r.next
        cur.next = pre
        if m == 1:
            start = cur

        return start
