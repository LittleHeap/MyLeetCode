class Solution:
    def numSquares(self, n: int) -> int:
        hold = []

        for i in range(1, n // 2 + 2):
            if i ** 2 <= n:
                hold.append(i ** 2)

        dp = [float('inf') for _ in range(n)]

        for ele in hold:
            dp[ele - 1] = 1

        if dp[-1] == 1:
            return 1

        for i in range(n):
            if dp[i] == 1:
                continue
            else:
                for step in hold:
                    if i - step >= 0:
                        dp[i] = min(dp[i], dp[i - step] + 1)

        return dp[-1]