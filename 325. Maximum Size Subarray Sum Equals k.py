class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:

        d = {}
        n = len(nums)
        for i in range(n):
            if i == 0:
                d[nums[i]] = i
                continue
            nums[i] += nums[i - 1]
            if nums[i] not in d:
                d[nums[i]] = i

        ans = 0
        for i in range(n - 1, -1, -1):
            if nums[i] == k:
                ans = max(ans, i + 1)
                continue
            if nums[i] - k in d:
                ans = max(ans, i - d[nums[i] - k])

        return ans