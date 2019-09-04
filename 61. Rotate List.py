# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or head.next is None:
            return head
        if k == 0:
            return head
        save = []
        while head:
            save.append(head)
            head = head.next
        k = k % len(save)
        if k == 0:
            return save[0]
        save[-k - 1].next = None
        save[-1].next = save[0]
        return save[-k]
