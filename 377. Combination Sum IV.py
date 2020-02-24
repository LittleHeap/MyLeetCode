class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        dp = [0 for _ in range(target)]

        for ele in nums:
            if ele < len(dp) + 1:
                dp[ele - 1] = 1

        for i in range(len(dp)):
            for step in nums:
                if i + step < len(dp):
                    dp[i + step] += dp[i]

        return dp[-1]