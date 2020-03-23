class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:

        n = len(nums)
        res = 0

        for i in range(32):
            count = 0
            for j in range(n):
                count += (nums[j] >> i) & 1
            res += count * (n - count)

        return res