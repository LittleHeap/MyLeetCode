class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort()

        n = len(intervals)
        m = n
        i = 1

        while i < n:
            if intervals[i][0] >= intervals[i - 1][0] and intervals[i][0] < intervals[i - 1][1]:
                if intervals[i][1] < intervals[i - 1][1]:
                    intervals.pop(i - 1)
                    n -= 1
                else:
                    intervals.pop(i)
                    n -= 1
            else:
                i += 1

        return m - n