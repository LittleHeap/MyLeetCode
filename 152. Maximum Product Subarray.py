class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        res = nums[0]
        dp = [[nums[0], nums[0]]]

        for i, ele in enumerate(nums):
            if i == 0:
                continue
            else:
                if ele >= 0:
                    large = max(ele, ele * dp[i - 1][0])
                    small = min(ele, ele * dp[i - 1][1])
                    res = max(res, large)
                    dp.append([large, small])
                else:
                    large = max(ele, ele * dp[i - 1][1])
                    small = min(ele, ele * dp[i - 1][0])
                    res = max(res, large)
                    dp.append([large, small])
        return res
