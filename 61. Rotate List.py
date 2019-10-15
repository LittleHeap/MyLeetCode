# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        hold = []
        while head:
            hold.append(head)
            head = head.next

        if not hold:
            return head

        n = len(hold)
        t = k % n

        hold[-1].next = hold[0]
        hold[-t - 1].next = None
        return hold[-t]
