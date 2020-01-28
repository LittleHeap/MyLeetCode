# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head

        pin = None

        a = None
        b = None

        start = head

        count = 0

        while head.next:
            count += 1
            if pin is None:
                pin = head.next
                a = head
                b = head.next
                head = head.next
                if b:
                    a.next = b.next
            else:
                a = head
                b = head.next
                head = head.next
                if b:
                    a.next = b.next

        if count % 2 == 1:
            a.next = pin
        else:
            b.next = pin

        return start