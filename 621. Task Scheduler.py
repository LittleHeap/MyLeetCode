class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        d = {}

        for ele in tasks:
            d[ele] = d.get(ele, 0) + 1

        hold = []

        for char, count in d.items():
            heapq.heappush(hold, (-count, char))

        res = 0
        while hold:
            temp = []
            for _ in range(n + 1):
                if not temp and not hold:
                    break
                else:
                    res += 1
                    if hold:
                        val, char = heapq.heappop(hold)
                        if val == -1:
                            pass
                        else:
                            temp.append((val + 1, char))

            hold = list(heapq.merge(hold, temp))

        return res