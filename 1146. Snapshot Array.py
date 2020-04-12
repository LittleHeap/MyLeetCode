class SnapshotArray:

    def __init__(self, length: int):

        self.s = 0
        self.d = defaultdict(list)
        for i in xrange(length):
            self.d[i].append([self.s, 0])
            self.d[i].append([self.s - 1, 0])

    def set(self, index: int, val: int) -> None:
        t = bisect.bisect_left(self.d[index], [self.s, 0])
        if t == len(self.d[index]):
            self.d[index].append([self.s, val])
        else:
            self.d[index][t][1] = val

    def snap(self) -> int:
        self.s += 1
        return self.s - 1

    def get(self, index: int, snap_id: int) -> int:
        t = bisect.bisect_left(self.d[index], [snap_id + 1, 0])
        return self.d[index][t - 1][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)