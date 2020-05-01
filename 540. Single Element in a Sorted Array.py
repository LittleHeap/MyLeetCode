class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        for i in range(1, len(nums), 2):
            if nums[i] != nums[i - 1]:
                return nums[i - 1]

        return nums[-1]