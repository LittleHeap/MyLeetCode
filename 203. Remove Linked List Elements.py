# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        if not head:
            return head

        start = head
        while head and head.val == val:
            start = head.next
            head = head.next

        while head:
            if head.next and head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next

        return start