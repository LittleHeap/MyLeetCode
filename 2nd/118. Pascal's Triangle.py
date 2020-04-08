class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows == 0:
            return []

        if numRows == 1:
            return [[1]]

        if numRows == 2:
            return [[1], [1, 1]]

        res = [[1], [1, 1]]

        for _ in range(numRows - 2):
            cur = [1]
            for i in range(len(res[-1]) - 1):
                cur.append(res[-1][i] + res[-1][i + 1])
            cur.append(1)
            res.append(cur)

        return res