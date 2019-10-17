class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        pre = 1
        n = len(nums)
        if n <= 1:
            return n
        i = 1

        while i < n:
            if nums[i] == nums[i - 1]:
                if pre == 1:
                    pre = 2
                    i += 1
                elif pre == 2:
                    nums.pop(i)
                    n -= 1
            else:
                pre = 1
                i += 1

        return n
