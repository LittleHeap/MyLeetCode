class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.ma = matrix

        m = len(self.ma)
        if m != 0:
            n = len(self.ma[0])
            for i in range(m):
                for j in range(1, n):
                    self.ma[i][j] += self.ma[i][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for i in range(row1, row2 + 1):
            if col1 - 1 < 0:
                res += self.ma[i][col2]
                continue
            res += self.ma[i][col2] - self.ma[i][col1 - 1]
        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)