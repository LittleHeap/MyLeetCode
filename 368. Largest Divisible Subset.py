class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        dp = [[] for i in range(len(nums))]

        nums.sort()
        dp[0].append(nums[0])

        n = 1
        res = [nums[0]]
        for i in range(1, len(nums)):
            l = 0
            cur = []
            for j in range(i - 1, -1, -1):
                if nums[i] % dp[j][-1] == 0 and len(dp[j]) > l:
                    l = len(dp[j])
                    cur = dp[j].copy()
            cur.append(nums[i])
            dp[i] = cur
            if len(cur) > n:
                n = len(cur)
                res = cur

        return res