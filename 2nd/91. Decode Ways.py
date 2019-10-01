class Solution:
    def numDecodings(self, s: str) -> int:
        if s == '':
            return 0

        dp = [0 for _ in range(len(s) + 1)]

        if s[0] == '0':
            return 0
        else:
            dp[0] = 1
            dp[1] = 1

        for i in range(2, len(s) + 1):
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]
                if int(s[i - 2:i]) <= 26 and s[i - 2] != '0':
                    dp[i] += dp[i - 2]
            else:
                if int(s[i - 2]) in [1, 2]:
                    dp[i] = dp[i - 2]
                else:
                    return 0

        return (dp[-1])


print(dp)
print(dp[-1])
