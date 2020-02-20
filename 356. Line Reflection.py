class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        d = {}

        for p in points:
            if p[1] not in d:
                d[p[1]] = []
            if p[0] not in d[p[1]]:
                d[p[1]].append(p[0])

        y = None
        for p in d:
            d[p].sort()
            if y is None:
                y = sum(d[p]) / len(d[p])
            if sum(d[p]) / len(d[p]) != y:
                return False
            for i in range(len(d[p]) // 2):
                if d[p][i] + d[p][len(d[p]) - 1 - i] != 2 * y:
                    return False

        return True