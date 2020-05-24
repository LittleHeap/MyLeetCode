class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:

        res = 0
        cur = 0

        for i, ele in enumerate(nums):
            if i == 0:
                res = 1
                cur = 1
            else:
                if nums[i] > nums[i - 1]:
                    cur += 1
                    res = max(res, cur)
                else:
                    cur = 1

        return res