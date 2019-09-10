# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0:
            return head

        cur = []

        start = head
        while head:
            if len(cur) < k + 1:
                cur.append(head)
            else:
                cur.pop(0)
                cur.append(head)
            head = head.next

        if len(cur) == k + 1:
            cur[0].next = None
            cur[-1].next = start
            return cur[1]
        elif len(cur) == k:
            return start
        else:
            k = k % len(cur)
            if k == 0:
                return start
            cur[-k - 1].next = None
            cur[-1].next = start
            return cur[-k]
