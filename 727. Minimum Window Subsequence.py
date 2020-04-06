class Solution:
    def minWindow(self, S: str, T: str) -> str:

        n = len(S)
        m = len(T)

        dp = [[float('inf') for _ in range(n + 1)] for _ in range(m + 1)]

        for j in range(n + 1):
            dp[0][j] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if T[i - 1] == S[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = dp[i][j - 1] + 1

        l = min(dp[-1])
        if l == float('inf'):
            return ''
        else:
            index = dp[-1].index(l)
            return S[index - l:index]        

