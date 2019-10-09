class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        index = 0

        n = len(nums)

        while index < n:
            if index == 0:
                index += 1
            else:
                if nums[index] == nums[index - 1]:
                    nums.pop(index)
                    n -= 1
                else:
                    index += 1

        return len(nums)
