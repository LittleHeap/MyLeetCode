class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        if s[::-1] == s:
            return len(s)

        dp = [0 for _ in range(len(s))]

        for i in range(len(s)):
            # print(dp)
            newdp = dp[:]
            newdp[i] = 1
            for j in range(i - 1, -1, -1):
                if s[j] == s[i]:
                    newdp[j] = 2 + dp[j + 1]
                else:
                    newdp[j] = max(newdp[j + 1], dp[j])
            dp = newdp

        # print(dp)
        return dp[0]


