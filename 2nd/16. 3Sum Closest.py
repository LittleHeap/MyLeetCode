class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        ans = float('inf')
        flag = 0
        for i in range(n - 2):
            l = i + 1
            r = n - 1
            t = target - nums[i]
            while l < r:
                if nums[l] + nums[r] > t:
                    if abs(t - nums[l] - nums[r]) < ans:
                        res = nums[i] + nums[l] + nums[r]
                        ans = abs(t - nums[l] - nums[r])
                    r -= 1
                elif nums[l] + nums[r] < t:
                    if abs(t - nums[l] - nums[r]) < ans:
                        res = nums[i] + nums[l] + nums[r]
                        ans = abs(t - nums[l] - nums[r])
                    l += 1
                else:
                    ans = 0
                    res = target
                    flag = 1
                    break
            if flag:
                break
        return res
