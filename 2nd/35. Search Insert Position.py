class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        ans = 0

        for i in range(len(nums)):
            if i == 0 and nums[i] > target:
                return 0
            if i > 0 and nums[i] > target and nums[i - 1] < target:
                return i
            if nums[i] == target:
                return i
        return i + 1
