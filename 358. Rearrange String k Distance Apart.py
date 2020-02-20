class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s

        d = collections.Counter(s)

        h = []
        for ele in d.items():
            heapq.heappush(h, [-ele[1], ele[0]])

        res = ''
        while h:
            if h and len(h) < k:
                for i in range(len(h)):
                    if h[i][0] < -1:
                        return ''
                    else:
                        res += h[i][1]
                return res
            hold = []
            for _ in range(k):
                hold.append(heapq.heappop(h))
                res += hold[-1][1]
                hold[-1][0] += 1
                if hold[-1][0] == 0:
                    hold.pop()
            for i in range(len(hold)):
                heapq.heappush(h, hold[i])

        return res