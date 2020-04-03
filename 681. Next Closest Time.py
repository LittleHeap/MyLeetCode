class Solution:
    def nextClosestTime(self, time: str) -> str:

        hour, minute = time.split(":")
        unique_digits = set(list(hour) + list(minute))
        if len(unique_digits) == 1: return time
        hour, minute = int(hour), int(minute)
        while True:
            minute += 1
            if minute == 60:
                minute = 0
                hour += 1
            hour %= 24
            strHour = str(hour)
            if len(strHour) == 1:
                strHour = "0" + strHour
            strMinute = str(minute)
            if len(strMinute) == 1:
                strMinute = "0" + strMinute
            uniq = set(strHour + strMinute)
            if uniq.issubset(unique_digits) or uniq == unique_digits:
                return strHour + ":" + strMinute