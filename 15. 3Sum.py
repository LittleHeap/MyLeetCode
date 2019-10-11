class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        n = len(nums)

        res = []
        for i in range(n - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            t = -nums[i]
            l = i + 1
            r = n - 1
            while l < r:
                if nums[l] + nums[r] == t:
                    res.append([nums[i], nums[r], nums[l]])
                    l += 1
                    while l < n and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1
                    while r >= 0 and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < t:
                    l += 1
                    while l < n and nums[l] == nums[l - 1]:
                        l += 1
                else:
                    r -= 1
                    while r >= 0 and nums[r] == nums[r + 1]:
                        r -= 1

        return res