class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        lr = []
        rl = []

        n = len(nums)

        cur = float('inf')
        for i in range(n):
            cur = min(cur, nums[i])
            lr.append(cur)

        cur = float('-inf')
        for i in range(n - 1, -1, -1):
            cur = max(cur, nums[i])
            rl.insert(0, cur)

        for i in range(n):
            if nums[i] > lr[i] and nums[i] < rl[i]:
                return 1

        return 0