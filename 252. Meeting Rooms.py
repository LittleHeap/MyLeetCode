class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        inter = sorted(intervals, key=lambda x: x[1])

        for i in range(1, len(inter)):
            if inter[i][0] < inter[i - 1][1]:
                return False
        return True

