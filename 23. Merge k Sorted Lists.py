# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        n = len(lists)
        i = n - 1
        while i >= 0:
            if lists[i] == None:
                lists.pop(i)
            i -= 1

        if not lists:
            return None

        val = []
        hold = []
        for i in range(len(lists)):
            val.append(lists[i].val)

        start = None
        while lists:
            index = val.index(min(val))
            node = ListNode(val[index])
            if start is None:
                start = node
                pre = node
            else:
                pre.next = node
                pre = node
            lists[index] = lists[index].next
            if lists[index] is None:
                lists.pop(index)
                val.pop(index)
            else:
                val[index] = lists[index].val
        return start