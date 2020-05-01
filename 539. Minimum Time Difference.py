class Solution:
    def findMinDifference(self, T: List[str]) -> int:

        hold = []

        for t in T:
            hour, minute = t.split(':')
            time = int(hour) * 60 + int(minute)
            hold.append(time)

        hold.sort()

        res = float('inf')
        for i in range(1, len(hold)):
            res = min(res, hold[i] - hold[i - 1])

        res = min(24 * 60 - (hold[-1] - hold[0]), res)

        return res