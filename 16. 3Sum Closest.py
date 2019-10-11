class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        n = len(nums)

        res = float('inf')
        dis = float('inf')
        for i in range(n - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = n - 1
            while r >= 0 and l < n and l < r:
                s = nums[i] + nums[l] + nums[r]
                curdis = abs(target - s)
                if curdis < dis:
                    res = s
                    dis = curdis
                if s == target:
                    return target
                elif s > target:
                    r -= 1
                    while r >= 0 and nums[r] == nums[r + 1]:
                        r -= 1
                elif s < target:
                    l += 1
                    while l < n and nums[l] == nums[l - 1]:
                        l += 1

        return res