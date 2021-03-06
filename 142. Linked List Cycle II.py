# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        if not head:
            return None

        node = []
        while head:
            node.append(head)
            head = head.next
            if head in node:
                return head

        return None
