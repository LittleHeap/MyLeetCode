# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        hold = []

        head = None
        pre = None

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(hold, [lists[i].val, i])

        while hold:
            if not head:
                [val, index] = heapq.heappop(hold)
                lists[index] = lists[index].next
                if lists[index]:
                    heapq.heappush(hold, [lists[index].val, index])
                head = ListNode(val)
                pre = head
            else:
                [val, index] = heapq.heappop(hold)
                lists[index] = lists[index].next
                if lists[index]:
                    heapq.heappush(hold, [lists[index].val, index])
                node = ListNode(val)
                pre.next = node
                pre = node

        return head