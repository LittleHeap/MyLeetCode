class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.res = []

    def addNum(self, val: int) -> None:

        if not self.res:
            self.res.append([val, val])

        for i in range(len(self.res)):
            if i == 0:
                if val < self.res[0][0] - 1:
                    self.res.insert(0, [val, val])
                    break
                elif val == self.res[0][0] - 1:
                    self.res[0][0] = val
                    break
            if i == len(self.res) - 1:
                if val > self.res[-1][1] + 1:
                    self.res.append([val, val])
                    break
                elif val == self.res[-1][1] + 1:
                    self.res[-1][-1] = val
                    break

            if val >= self.res[i][0] and val <= self.res[i][1]:
                break
            elif val > self.res[i][1] + 1 and val < self.res[i + 1][0] - 1:
                self.res.insert(i + 1, [val, val])
                break
            elif val == self.res[i][1] + 1 and val == self.res[i + 1][0] - 1:
                self.res[i][1] = self.res[i + 1][1]
                self.res.pop(i + 1)
                break
            elif val == self.res[i][1] + 1:
                self.res[i][1] = val
                break
            elif val == self.res[i + 1][0] - 1:
                self.res[i + 1][0] = val
                break

    def getIntervals(self) -> List[List[int]]:

        return self.res

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()