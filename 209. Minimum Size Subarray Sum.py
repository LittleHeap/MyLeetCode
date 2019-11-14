class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0

        l = 0
        r = 0
        cur = 0
        ans = float('inf')
        for i in range(len(nums)):
            cur += nums[i]
            r = i
            if cur >= s:
                while cur - nums[l] >= s:
                    cur -= nums[l]
                    l += 1
                ans = min(ans, r - l + 1)
        if ans == float('inf'):
            return 0
        else:
            return ans