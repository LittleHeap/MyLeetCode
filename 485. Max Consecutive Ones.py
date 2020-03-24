class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        if not nums:
            return 0

        ans = 0
        cur = 0
        for ele in nums:
            if ele == 1:
                cur = cur + 1
            else:
                ans = max(ans, cur)
                cur = 0
        ans = max(ans, cur)
        return ans
