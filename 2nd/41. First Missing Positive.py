class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ans = 1
        hold = set()
        for ele in nums:
            if ele > 0:
                hold.add(ele)
                while ans in hold:
                    ans += 1
        return ans