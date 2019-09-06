class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:

        save = {}
        big = 0
        if not ops:
            return m * n

        row = m
        col = n
        c = 0

        for ele in ops:
            row = min(row, ele[0])
            col = min(col, ele[1])
            c += 1

        return row * col
