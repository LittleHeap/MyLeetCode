class Solution:
    def findIntegers(self, num: int) -> int:

        temp = str(bin(num))[2:]
        dp = [[0, 0] for _ in range(len(temp))]

        dp[-1][0] = 1
        dp[-1][1] = 1

        res = (1 if temp[-1] == '0' else 2)
        for i in range(len(temp) - 2, -1, -1):
            dp[i][0] = dp[i + 1][0] + dp[i + 1][1]
            dp[i][1] = dp[i + 1][0]
            if temp[i] == '1':
                if temp[i + 1] == '0':
                    res += dp[i + 1][0] + dp[i + 1][1]
                else:
                    res = dp[i][0] + dp[i][1]

        return res