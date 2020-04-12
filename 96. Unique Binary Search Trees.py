class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 1

        dp = [1, 2]

        if n <= 2:
            return dp[n - 1]
        else:
            for i in range(3, n + 1):
                res = 0
                for k in range(1, i):
                    res += dp[k - 1] * (dp[i - k - 2] if i - k - 2 >= 0 else 1)
                res += dp[i - 2]
                dp.append(res)

        return dp[-1]
