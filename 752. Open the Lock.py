class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        deadends = set(deadends)

        if target in deadends or '0000' in deadends:
            return -1
        elif target == '0000':
            return 0

        q = [('0000', 0)]

        done = set()
        done.add('0000')

        while q:
            newq = []
            for cur, times in q:
                cur = list(cur)
                for i in range(4):
                    for k in [-1, 1]:
                        newcur = cur.copy()
                        newcur[i] = str((int(newcur[i]) + k) % 10)
                        newcur = ''.join(newcur)
                        if newcur == target:
                            return times + 1
                        if newcur in deadends or newcur in done:
                            continue
                        else:
                            newq.append((newcur, times + 1))
                            done.add(newcur)
            q = newq

        return -1
