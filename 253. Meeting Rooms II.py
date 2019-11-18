class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        inter = sorted(intervals, key=lambda x: x[0])

        ans = 0

        while inter:
            i = 0
            n = len(inter)
            cur = inter[i]
            inter.pop(0)
            n -= 1
            while i < n:
                if inter[i][0] >= cur[1]:
                    cur = inter.pop(i)
                    n -= 1
                else:
                    i += 1
            ans += 1
        return ans
