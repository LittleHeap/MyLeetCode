# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if not head:
            return head

        start = head
        pre = head
        head = head.next
        while head:
            if head.val == pre.val:
                head = head.next
                pre.next = head
            else:
                pre = head
                head = head.next
        return start
