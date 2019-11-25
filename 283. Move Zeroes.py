class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        index = 0
        n = len(nums)
        i = 0

        while index < n:
            index += 1
            if nums[i] == 0:
                nums.append(nums.pop(i))
            else:
                i += 1
