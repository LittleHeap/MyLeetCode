class Solution:
    def checkRecord(self, n: int) -> int:

        if n == 0:
            return 1
        if n == 1:
            return 3

        dp = [[[1, 1, 1], [0, 0, 0]], [[2, 2, 2], [0, 1, 1]]]

        m = 10 ** 9 + 7
        for i in range(n - 2):
            new = [[0, 0, 0], [0, 0, 0]]
            new[0][0] = (dp[-1][0][1] + dp[-1][0][2]) % m
            new[0][1] = (dp[-1][0][2] + dp[-2][0][2]) % m
            new[0][2] = (dp[-1][0][1] + dp[-1][0][2]) % m
            new[1][0] = 0
            new[1][1] = (dp[-1][0][0] + dp[-1][1][2] + dp[-2][0][0] + dp[-2][1][2]) % m
            new[1][2] = (dp[-1][0][0] + dp[-1][1][1] + dp[-1][1][2]) % m
            dp.pop(0)
            dp.append(new)

        return (sum(dp[-1][0]) + sum(dp[-1][1])) % m