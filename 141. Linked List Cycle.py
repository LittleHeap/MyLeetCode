# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        if not head:
            return False

        node = []
        while head:
            node.append(head)
            head = head.next
            if head in node:
                return True
        return False
