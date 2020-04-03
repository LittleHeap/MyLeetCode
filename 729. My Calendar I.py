class MyCalendar:

    def __init__(self):
        self.l = []

    def book(self, start: int, end: int) -> bool:
        index = bisect.bisect_right(self.l, (start, end))
        if index - 1 >= 0:
            if self.l[index - 1][1] > start:
                return False
        if index < len(self.l):
            if self.l[index][0] < end:
                return False

        self.l.insert(index, (start, end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)