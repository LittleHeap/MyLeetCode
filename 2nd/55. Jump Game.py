class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return True
        target = n - 1

        far = 0

        for i in range(n):
            if i > far:
                return False
            if i + nums[i] <= far:
                continue
            else:
                far = i + nums[i]
            if far >= target:
                return True
