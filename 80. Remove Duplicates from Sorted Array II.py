class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        c = 1
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                c += 1
                if c == 3:
                    nums.pop(i)
                    c -= 1
                    i -= 1
            else:
                c = 1

            i += 1

