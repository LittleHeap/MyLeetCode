class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:

        d = defaultdict(int)

        for i in range(len(wall)):
            cur = 0
            for j in range(len(wall[i]) - 1):
                cur += wall[i][j]
                d[cur] += 1

        if not d:
            return len(wall)

        res = max(d.values())

        return len(wall) - res