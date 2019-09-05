# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        if head.next is None:
            return head
        else:
            start = head.next
            pre = None
            while head:
                if head.next is not None:
                    if pre is None:
                        pre = head
                    elif head.next:
                        pre.next = head.next
                        pre = head
                    head.next.next, head.next, head = head, head.next.next, head.next.next
                else:
                    head = head.next
            return start
