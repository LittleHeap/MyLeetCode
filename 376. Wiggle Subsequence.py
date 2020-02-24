class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:

        if not nums:
            return 0

        dp = [[1, 1] for _ in range(len(nums))]
        res = 1

        for i in range(1, len(nums)):
            big = 0
            small = 0
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    dp[i][0] = max(dp[i][0], dp[j][1] + 1)
                    small = 1
                elif nums[j] > nums[i]:
                    dp[i][1] = max(dp[i][1], dp[j][0] + 1)
                    big = 1
                if big and small:
                    break
            res = max(res, max(dp[i]))

        return res