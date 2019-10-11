class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        res = 1

        hold = set()
        for ele in nums:
            hold.add(ele)
            while res in hold:
                res += 1

        return res