class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort()

        res = 1
        line = points[0][1]

        for i in range(1, len(points)):
            if points[i][0] <= line:
                if points[i][1] >= line:
                    continue
                else:
                    line = points[i][1]
            else:
                res += 1
                line = points[i][1]

        return res