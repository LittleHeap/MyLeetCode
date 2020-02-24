class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ds = {}
        dt = {}

        for ele in s:
            ds[ele] = ds.get(ele, 0) + 1

        for ele in t:
            if ele not in ds:
                return ele
            dt[ele] = dt.get(ele, 0) + 1
            if dt[ele] > ds[ele]:
                return ele