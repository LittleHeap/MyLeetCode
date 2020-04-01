class Solution:
    def reorganizeString(self, S: str) -> str:
        d = collections.Counter(S)

        hold = []
        for char, count in d.items():
            heapq.heappush(hold, (-count, char))

        res = ''
        while hold:
            cur = []
            if res == '':
                val, char = heapq.heappop(hold)
                res += char
                if val < -1:
                    heapq.heappush(hold, (val + 1, char))
            else:
                cur = []
                while hold and hold[0][1] == res[-1]:
                    cur.append(heapq.heappop(hold))
                if not hold:
                    return ''
                else:
                    val, char = heapq.heappop(hold)
                    res += char
                    if val < -1:
                        heapq.heappush(hold, (val + 1, char))
                hold = list(heapq.merge(cur, hold))

        return res




