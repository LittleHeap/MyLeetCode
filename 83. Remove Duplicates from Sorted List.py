# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        res = head

        while head:
            if head.next and head.val == head.next.val:
                cur = head.next
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                head.next = cur.next
                head = cur.next
            else:
                head = head.next

        return res
