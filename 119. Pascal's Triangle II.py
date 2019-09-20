class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        res = [[1 for _ in range(i + 1)] for i in range(rowIndex + 1)]

        for i in range(rowIndex + 1):
            if i <= 1:
                continue
            for k in range(1, i):
                res[i][k] = res[i - 1][k - 1] + res[i - 1][k]

        return res[rowIndex]
