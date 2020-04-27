class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        d = {0: -1}

        zero = 0
        one = 0

        res = 0

        for i, ele in enumerate(nums):
            if ele == 0:
                zero += 1
            else:
                one += 1
            key = zero - one
            if key in d:
                res = max(res, i - d[key])
            else:
                d[key] = i

        return res