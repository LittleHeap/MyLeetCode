class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        self.d[key] = val

    def sum(self, prefix: str) -> int:
        res = 0
        for key, val in self.d.items():
            res += (val if key.find(prefix) == 0 else 0)
        return res

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)