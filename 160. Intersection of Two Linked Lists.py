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
        if headA == headB:
            return headA

        la = []
        lb = []
        while headA:
            la.append(headA)
            headA = headA.next

        while headB:
            lb.append(headB)
            headB = headB.next

        la.reverse()
        lb.reverse()
        n = min(len(la), len(lb))
        for i in range(n):
            if la[i] != lb[i]:
                if i == 0:
                    return None
                else:
                    return la[i - 1]
        if len(la) < len(lb):
            if la:
                return la[-1]
            else:
                return None
        else:
            if lb:
                return lb[-1]
            else:
                return None