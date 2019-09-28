class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        cur = 0
        for i in range(n):
            cur += nums[i]
            if cur >= s:
                break
        if i == n - 1 and cur < s:
            return 0
        res = i + 1
        l = 0
        while cur - nums[l] >= s:
            cur -= nums[l]
            l += 1
            res = i - l + 1
        for r in range(i + 1, n):
            cur -= nums[l]
            cur += nums[r]
            l += 1
            while cur - nums[l] >= s:
                cur -= nums[l]
                l += 1
            res = r - l + 1

        return res