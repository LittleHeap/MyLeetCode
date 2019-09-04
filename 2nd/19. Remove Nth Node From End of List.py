# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        save = []
        start = head
        while head:
            if len(save) < n + 1:
                save.append(head)
                head = head.next
            else:
                save.pop(0)
                save.append(head)
                head = head.next
        if len(save) == n + 1:
            save[0].next = save[0].next.next
            save[1].next = None
            return start
        else:
            # 考虑元素装不满队列的情况
            return save[0].next
