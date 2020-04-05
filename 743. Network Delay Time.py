class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:

        d = {}
        for i in range(1, N + 1):
            d[i] = float('inf')

        c = defaultdict(list)
        for start, end, time in times:
            bisect.insort(c[start], (time, end))

        def deep(node, cur):
            for time, nextnode in c[node]:
                if d[node] + time < d[nextnode]:
                    d[nextnode] = d[node] + time
                    deep(nextnode, d[node] + time)

        d[K] = 0
        deep(K, 0)

        if float('inf') in d.values():
            return -1
        else:
            return max(d.values())


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:

        d = {}
        for i in range(1, N + 1):
            d[i] = float('inf')

        c = defaultdict(list)
        for start, end, time in times:
            c[start].append((time, end))

        d[K] = 0
        q = [(K, d[K])]
        while q:
            newq = []
            for node, cur in q:
                for time, nextnode in c[node]:
                    if cur + time < d[nextnode]:
                        d[nextnode] = cur + time
                        newq.append((nextnode, d[nextnode]))
            q = newq

        if float('inf') in d.values():
            return -1
        else:
            return max(d.values())