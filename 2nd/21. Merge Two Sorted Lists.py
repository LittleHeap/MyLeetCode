# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        start = l2
        if l1 and not l2:
            return l1
        pre = None
        while l1 and l2:
            if l2.val <= l1.val:
                pre = l2
                l2 = l2.next
            else:
                if pre is None:
                    start = ListNode(l1.val)
                    start.next = l2
                    pre = start
                    l1 = l1.next
                else:
                    pre.next = ListNode(l1.val)
                    pre = pre.next
                    pre.next = l2
                    l1 = l1.next
        if l1:
            pre.next = l1
        return start