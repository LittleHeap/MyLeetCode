# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:

        if not head:
            return head
        res = []

        while head:
            res.append(head)
            head = head.next

        for i in range(len(res)):
            temp = res[i]
            index = i
            while index - 1 >= 0:
                if temp.val < res[index - 1].val:
                    res[index] = res[index - 1]
                    index -= 1
                else:
                    res[index] = temp
                    break
            if index == 0:
                res[index] = temp

        res.append(None)
        for i in range(len(res) - 1):
            res[i].next = res[i + 1]

        return res[0]
