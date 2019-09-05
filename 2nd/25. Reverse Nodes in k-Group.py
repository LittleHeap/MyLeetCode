# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        if not head or k == 1:
            return head

        pre = None
        start = head

        while head:
            cur = []
            c = 0
            while 1:
                cur.append(head)
                c += 1
                if head is None or c == k + 1:
                    break
                head = head.next
            if c - 1 < k:
                return start
            else:
                if pre is None:
                    pre = cur[0]
                    start = cur[-2]
                else:
                    pre.next = cur[-2]
                    pre = cur[0]
                for j in range(k - 1, 0, -1):
                    cur[j].next = cur[j - 1]
                cur[0].next = cur[-1]

        return start



