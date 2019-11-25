class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []
        self.n = 0

    def addNum(self, num: int) -> None:
        if not self.l:
            self.l.append(num)
            self.n += 1
        else:
            l = 0
            r = self.n - 1
            while l < r:
                mid = (l + r) // 2
                if self.l[mid] == num:
                    break
                elif self.l[mid] > num:
                    r = mid
                else:
                    l = mid + 1
            mid = (l + r) // 2
            if self.l[mid] >= num:
                self.l.insert(mid, num)
            else:
                self.l.insert(mid + 1, num)
            self.n += 1

    def findMedian(self) -> float:
        if self.n % 2 == 1:
            return float(self.l[self.n // 2])
        else:
            return (float(self.l[self.n // 2]) + float(self.l[self.n // 2 - 1])) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()