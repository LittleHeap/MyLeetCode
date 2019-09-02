nums = [1, 1, 1, 1, 1]
S = 3

dp = [{} for _ in range(len(nums) + 1)]
dp[0][0] = 1
print(dp)

for i in range(1, len(nums) + 1):
    for ele in dp[i - 1]:
        dp[i][ele + nums[i - 1]] = dp[i].get(ele + nums[i - 1], 0) + dp[i - 1].get(ele)
        dp[i][ele - nums[i - 1]] = dp[i].get(ele - nums[i - 1], 0) + dp[i - 1].get(ele)

print(dp[-1].get(S))
