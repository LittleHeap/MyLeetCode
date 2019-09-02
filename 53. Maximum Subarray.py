nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

dp = [[-float('inf'), -float('inf')] for _ in range(len(nums) + 1)]

res = -float('inf')
for i in range(1, len(nums) + 1):
    dp[i][1] = max(dp[i - 1][1] + nums[i - 1], nums[i - 1])
    dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
    res = max(res, max(dp[i][1], dp[i][0]))

print(dp)
print(res)
