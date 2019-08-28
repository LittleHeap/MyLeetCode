# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a = []
        while headA:
            a.append(headA)
            headA = headA.next
        b = []
        while headB:
            b.append(headB)
            headB = headB.next
        if len(a) == 0 or len(b) == 0:
            return None
        i = -1
        pre = None
        while True:
            if abs(i) > min(len(a), len(b)):
                return pre
            if a[i] == b[i]:
                pre = a[i]
                i = i - 1
            else:
                return pre
