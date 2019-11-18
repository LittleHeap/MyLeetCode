class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = {}
        dt = {}

        for c in s:
            ds[c] = ds.get(c, 0) + 1

        for c in t:
            dt[c] = dt.get(c, 0) + 1

        return ds == dt