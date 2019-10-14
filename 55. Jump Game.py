class Solution:
    def canJump(self, nums: List[int]) -> bool:

        far = 0
        n = len(nums)
        if n <= 1:
            return True

        dp = [0 for _ in range(n)]

        for i in range(len(nums)):
            if far < i:
                return False
            if nums[i] + i <= far:
                continue
            for k in range(far + 1, i + nums[i] + 1):
                if k >= n:
                    break
                dp[k] = dp[i] + 1
            far = i + nums[i]
            if dp[-1] > 0:
                return True
