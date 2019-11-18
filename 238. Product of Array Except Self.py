class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        n = len(nums)
        lr = [nums[0]]
        for i in range(1, n):
            lr.append(nums[i] * lr[-1])

        rl = [nums[-1]]
        for i in range(n - 2, -1, -1):
            rl.append(nums[i] * rl[-1])

        rl.reverse()

        res = []
        for i in range(n):
            l, r = 0, 0
            if i - 1 < 0:
                l = 1
            else:
                l = lr[i - 1]
            if i + 1 >= n:
                r = 1
            else:
                r = rl[i + 1]
            res.append(l * r)
        return res