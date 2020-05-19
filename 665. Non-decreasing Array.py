class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:

        temp = 1
        for i in range(1, len(nums)):
            if nums[i] >= nums[i - 1]:
                continue
            elif temp:
                temp -= 1
                if i - 2 >= 0 and nums[i - 2] <= nums[i] or i == 1:
                    continue
                else:
                    nums[i] = nums[i - 1]
            else:
                return False
        return True
