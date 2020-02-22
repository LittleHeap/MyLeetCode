# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:

        if not head:
            return head

        start = head
        l = []
        while head:
            l.append(head)
            head = head.next

        flag = 0
        for i in range(len(l) - 1, -1, -1):
            if l[i].val + 1 <= 9:
                l[i].val += 1
                flag = 0
                break
            else:
                l[i].val = 0
                flag = 1

        if flag:
            new = ListNode(1)
            new.next = start
            return new
        else:
            return start