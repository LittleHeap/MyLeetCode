# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


import heapq


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None

        cur = []

        for head in lists:
            cur.append(head)

        heap = []
        n = len(cur)
        for i in range(n):
            if cur[i] is not None:
                heapq.heappush(heap, (cur[i].val, i))

        pre = None
        start = None
        while heap:
            now = heapq.heappop(heap)
            cur[now[1]] = cur[now[1]].next
            if pre is None:
                node = ListNode(now[0])
                start = node
                pre = node
            else:
                node = ListNode(now[0])
                pre.next = node
                pre = pre.next
            if cur[now[1]] is not None:
                heapq.heappush(heap, (cur[now[1]].val, now[1]))

        return start
