class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        res = 0
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            l = i + 1
            r = n - 1
            while l < r:
                s = sum([nums[i], nums[l], nums[r]])
                if s >= target:
                    r -= 1
                else:
                    res += r - l
                    l += 1
        return res