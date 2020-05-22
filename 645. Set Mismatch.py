class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hold = (1 + len(nums)) * len(nums) // 2

        temp = sum(list(set(nums)))

        miss = hold - temp

        du = sum(nums) - temp

        return [du, miss]