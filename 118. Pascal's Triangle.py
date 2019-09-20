class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        res = [[1 for _ in range(i + 1)] for i in range(numRows)]

        for i in range(numRows):
            if i <= 1:
                continue
            for k in range(1, i):
                res[i][k] = res[i - 1][k - 1] + res[i - 1][k]

        return (res)
