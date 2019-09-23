class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)

        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1

        return i
