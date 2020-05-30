class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        res, cur, j = 0, 1, 0

        for i, num in enumerate(nums):
            cur *= num
            if cur >= k:
                while j <= i and cur >= k:
                    cur = cur // nums[j]
                    j += 1
            res += i - j + 1

        return res