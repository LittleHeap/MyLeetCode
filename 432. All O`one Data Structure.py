class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        self.d[key] = self.d.get(key, 0) + 1

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key not in self.d:
            pass
        else:
            if self.d[key] == 1:
                del self.d[key]
            else:
                self.d[key] -= 1

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if not self.d:
            return ''
        else:
            cur = float('-inf')
            res = ''
            for key, val in self.d.items():
                if val > cur:
                    res = key
                    cur = val

            return res

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        cur = float('inf')
        res = ''
        for key, val in self.d.items():
            if val < cur:
                res = key
                cur = val

        return res

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()