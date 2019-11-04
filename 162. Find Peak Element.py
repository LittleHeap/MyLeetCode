class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(1, n + 1):
            if i == n:
                return n - 1
            if nums[i] < nums[i - 1]:
                return i - 1

        return 0