# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        start = head
        pre = None
        while head:
            if head.val == val:
                if pre == None:
                    head = head.next
                    start = head
                else:
                    pre.next, head.next, head  = head.next, None, head.next
            else:
                pre, head = head, head.next
        return start