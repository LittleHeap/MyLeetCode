class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        # 行是s字符串
        n = len(s) + 1
        # 列是t字符串
        m = len(t) + 1

        dp = [[0] * n for _ in range(m)]

        # 初始化问题注意，只初始化第一行，第一列不动
        for j in range(n):
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(i, n):
                # 前提还是最后一个字母可以对应上再细化
                if t[i - 1] == s[j - 1]:
                    if i == j:
                        # 转换长度相等时候，最后一个字母必须对应用上，就只能从i-1 j-1继承
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        # 转换长度富余时，最后一个字母用上就是i-1 j-1，不用就是i j-1，两种情况
                        dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
                else:
                    # 否则将当前行最大长度延伸到末尾
                    dp[i][j] = dp[i][j - 1]

        return dp[-1][-1]