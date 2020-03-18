# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        if not l1:
            return l2
        if not l2:
            return l1

        a = []
        b = []

        while l1:
            a.append(l1)
            l1 = l1.next
        while l2:
            b.append(l2)
            l2 = l2.next

        if len(a) < len(b):
            a, b = b, a

        ia = len(a) - 1
        ib = len(b) - 1

        flag = 0
        while ib >= 0:
            a[ia].val += b[ib].val + flag
            if a[ia].val >= 10:
                flag = 1
                a[ia].val -= 10
            else:
                flag = 0
            ia -= 1
            ib -= 1

        if ia >= 0:
            while ia >= 0 and a[ia].val + flag >= 10:
                a[ia].val = 0
                flag = 1
                ia -= 1
            if ia >= 0:
                a[ia].val += flag
                flag = 0

        if ia == -1 and flag:
            start = ListNode(1)
            start.next = a[0]
            return start
        else:
            return a[0]







