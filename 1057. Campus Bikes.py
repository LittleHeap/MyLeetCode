class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        hold = []

        wset = set(i for i in range(len(workers)))
        bset = set(i for i in range(len(bikes)))

        for i, (wx, wy) in enumerate(workers):
            for j, (bx, by) in enumerate(bikes):
                hold.append((abs(wx - bx) + abs(wy - by), i, j))

        hold.sort()

        res = [None for _ in range(len(workers))]
        for d, w, b in hold:
            if w not in wset or b not in bset:
                continue
            else:
                res[w] = b
                wset.remove(w)
                bset.remove(b)

        return res