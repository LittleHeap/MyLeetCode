class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.win = []
        self.s = 0

    def next(self, val: int) -> float:
        if len(self.win) < self.size:
            self.win.append(val)
            self.s += val
        else:
            self.s -= self.win.pop(0)
            self.win.append(val)
            self.s += val
        return self.s/len(self.win)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)