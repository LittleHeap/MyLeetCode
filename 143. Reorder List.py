# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None

        res = []

        start = head
        while head:
            res.append(head)
            head = head.next

        i = 0
        n = len(res)
        if n <= 1:
            return start

        while i != n // 2 - 1:
            res[i].next = res[n - i - 1]
            res[n - i - 1].next = res[i + 1]
            i += 1

        if n % 2 == 0:
            res[i + 1].next = None
        else:
            res[i].next = res[i + 2]
            res[i + 2].next = res[i + 1]
            res[i + 1].next = None

        return start
