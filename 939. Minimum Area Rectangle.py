class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:

        n = len(points)

        nx = len(set(x for x, y in points))

        ny = len(set(y for x, y in points))

        if nx == n or ny == n:
            return 0

        res = float('inf')

        markx = {}

        save = defaultdict(list)

        for x, y in points:
            bisect.insort_right(save[x], y)

        for x in sorted(list(save.keys())):
            for i in range(len(save[x]) - 1):
                for j in range(i + 1, len(save[x])):
                    y1, y2 = save[x][i], save[x][j]
                    if (y1, y2) in markx:
                        area = (x - markx[(y1, y2)]) * (y2 - y1)
                        res = min(area, res)
                    markx[(y1, y2)] = x

        return res if res != float('inf') else 0

