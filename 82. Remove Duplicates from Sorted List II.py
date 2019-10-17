# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        res = head
        pre = None

        while head:
            if head.next and head.val == head.next.val:
                r = head.next
                while r.next and r.val == r.next.val:
                    r = r.next
                if pre == None:
                    res = r.next
                    head = r.next
                else:
                    head = r.next
                    pre.next = head
            else:
                pre = head
                head = head.next

        return res

