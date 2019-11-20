class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        hold = set(nums)

        for i in range(100000000000):
            if i not in hold:
                return i