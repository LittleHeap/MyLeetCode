class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:

        hold = []
        dist = float('inf')
        index = 0
        total = 0
        for i, (x, y) in enumerate(nuts):
            a = abs(x - tree[0]) + abs(y - tree[1])
            b = abs(x - squirrel[0]) + abs(y - squirrel[1])
            if -a + b < dist:
                dist = -a + b
                index = i
            total += a * 2
            hold.append((a, b))

        total = total - hold[index][0] + hold[index][1]

        return total