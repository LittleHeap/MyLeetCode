class Solution:
    def maximumGap(self, nums: List[int]) -> int:

        if len(nums) <= 1:
            return 0

        nums.sort()

        pre = nums[-1]
        nums.pop()

        ans = 0
        while nums:
            temp = nums.pop()
            ans = max(ans, pre - temp)
            pre = temp

        return ans
