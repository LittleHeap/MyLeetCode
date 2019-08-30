nums = [1, 2, 5, 6]

nums.sort()
nums.reverse()
dp = [[set(), set()] for _ in range(len(nums) + 1)]
dp[0][0].add(0)
dp[0][1].add(0)

s = sum(nums)
if s % 2 == 1:
    print(False)
else:
    target = int(s / 2)

for i in range(len(nums)):
    dp[i + 1][0] = dp[i][0] | dp[i][1]
    for ele in dp[i + 1][0]:
        dp[i + 1][1].add(ele + nums[i])
        if ele + nums[i] == target:
            print(True)
print(False)

print(dp)
