# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        node = []
        while head:
            node.append(head)
            head = head.next

        for i in range(len(node)):
            l = i - 1
            temp = node[i]
            while l >= 0 and temp.val < node[l].val:
                node[l + 1] = node[l]
                l -= 1
            node[l + 1] = temp

        for i in range(len(node) - 1):
            node[i].next = node[i + 1]

        node[-1].next = None
        return node[0]
