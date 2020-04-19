class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        m = len(p)
        n = len(s)

        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]

        dp[0][0] = True

        for i in range(1, m + 1):
            if any(dp[i - 1]) == False:
                return False
            for j in range(n + 1):
                if p[i - 1] == '?':
                    dp[i][j] = (False if j == 0 else dp[i - 1][j - 1])
                elif j - 1 >= 0 and p[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[i - 1] == '*':
                    dp[i][j] = (dp[i - 1][j] if j == 0 else (dp[i - 1][j - 1] or dp[i][j - 1] or dp[i - 1][j]))

        # print(dp)
        return dp[-1][-1]