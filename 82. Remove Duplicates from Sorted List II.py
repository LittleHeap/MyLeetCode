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
        while (head and head.next) and (head.val == head.next.val):
            while (head and head.next) and (head.val == head.next.val):
                head = head.next
            head = head.next
            start = head
        cur = []
        while head and head.next:
            if head.val == head.next.val:
                temp = head.next
                while (temp and temp.next) and (temp.val == temp.next.val):
                    temp = temp.next
                pre.next = temp.next
                head = temp.next
            else:
                pre = head
                head = head.next
        return start