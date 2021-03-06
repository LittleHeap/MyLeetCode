class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        m = len(p)
        n = len(s)

        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]

        dp[0][0] = True

        for i in range(1, m + 1):
            for j in range(n + 1):
                if p[i - 1] == '.':
                    dp[i][j] = (False if j == 0 else dp[i - 1][j - 1])
                elif j - 1 >= 0 and p[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[i - 1] == '*':
                    dp[i][j] = (dp[i - 1][j] if i - 1 >= 0 else False) or (dp[i - 2][j] if i - 2 >= 0 else False)
                    if i - 2 >= 0 and j - 1 >= 0 and (p[i - 2] == s[j - 1] or p[i - 2] == '.'):
                        dp[i][j] = dp[i][j] or dp[i][j - 1]

        return dp[-1][-1]