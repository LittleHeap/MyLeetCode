# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:

        if not head:
            return head

        node = head
        pre = None
        while head:
            if head.val >= x:
                pre = head
                head = head.next
            else:
                break

        if not head:
            return node

        if node != head:
            start = head
            pre.next = head.next
            head = head.next
            start.next = node
            node = start
        else:
            start = head
            head = head.next

        while head:
            if head.val < x:
                if pre:
                    pre.next = head.next
                    node.next, head.next = head, node.next
                    node = node.next
                    head = pre
                else:
                    node = node.next
                    head = head.next
            else:
                pre = head
                head = head.next
        return start
