# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        b = 0
        start = l2
        while l1 or l2:
            if l1 and l2:
                l2.val = l2.val + l1.val + b
            elif l2:
                l2.val = l2.val + b
            else:
                l2 = ListNode(l1.val)
                pre2.next = l2
                l2.val = l2.val + b
            if l2.val >= 10:
                l2.val = l2.val % 10
                b = 1
            else:
                b = 0
            pre1 = l1
            pre2 = l2
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if b == 1:
            pre2.next = ListNode(1)
        return start
