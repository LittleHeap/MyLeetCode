class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        for ele in nums:
            cur = 1
            if ele - 1 not in nums:
                while ele + 1 in nums:
                    ele = ele + 1
                    cur = cur + 1
                ans = max(ans, cur)
        return ans
