# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        if not head:
            return head

        start = head.next

        pre = None
        while head:
            cur1 = head
            cur2 = head.next
            if not cur2:
                if pre is not None:
                    pre.next = cur1
                    return start
                else:
                    return head
            else:
                if pre is not None:
                    pre.next, head, cur2.next, cur1.next, pre = cur2, cur2.next, cur1, None, cur1
                else:
                    pre, cur1.next, cur2.next, head = cur1, None, cur1, cur2.next

        return start
