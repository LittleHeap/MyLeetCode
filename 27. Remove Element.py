class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        index = 0
        n = len(nums)

        while index < n:
            if nums[index] == val:
                nums.pop(index)
                n -= 1
            else:
                index += 1

        return len(nums)