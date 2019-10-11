# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        if l1 and not l2:
            return l1
        elif not l1 and l2:
            return l2
        elif not l1 and not l2:
            return l1

        start = l1
        pre = None
        while l1 or l2:
            if l1 and l2:
                if l1.val <= l2.val:
                    pre = l1
                    l1 = l1.next
                else:
                    if pre is not None:
                        pre.next, l2.next, l2, pre = l2, l1, l2.next, l2
                    else:
                        start = l2
                        l2.next, l2, pre = l1, l2.next, start
            elif l1 and not l2:
                return start
            else:
                pre.next = l2
                return start
        return start