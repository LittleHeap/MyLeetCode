class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if not stones or stones[0] != 0:
            return 0

        s = set(stones)

        d = {}
        d[0] = set()
        d[0].add(1)

        while 1:
            if len(d) == 0:
                return 0
            else:
                for t in stones:
                    if t in d:
                        for step in d[t]:
                            next = t + step
                            if next == t:
                                continue
                            if next in s:
                                if next in d:
                                    d[next].add(step)
                                    d[next].add(step + 1)
                                    d[next].add(step - 1)
                                else:
                                    d[next] = set()
                                    d[next].add(step)
                                    d[next].add(step + 1)
                                    d[next].add(step - 1)
                        if stones[-1] in d:
                            return 1
                        del d[t]