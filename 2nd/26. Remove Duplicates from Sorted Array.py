class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        i = 0
        while i + 1 < n:
            if nums[i] == nums[i + 1]:
                nums.pop(i)
                n -= 1
            else:
                i += 1
        return len(nums)