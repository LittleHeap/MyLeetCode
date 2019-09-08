class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ans = 1
        save = set()
        for ele in nums:
            if ele > 0:
                save.add(ele)
            while ans in save:
                ans += 1
        return ans
