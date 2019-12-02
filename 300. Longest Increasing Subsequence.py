import sys
import bisect

nums = [10, 9, 2, 5, 3, 7, 101, 18]

dp = [float('inf')] * len(nums)
print(dp)

for x in nums:
    dp[bisect.bisect_left(dp, x)] = x
    print(dp)
print(dp)
print(bisect.bisect(dp, max(nums)))
