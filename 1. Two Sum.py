class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        save = {}
        for i in range(len(nums)):
            save[nums[i]] = i

        res = []
        for i in range(len(nums)):
            if save.get(target - nums[i]) is not None and save.get(target - nums[i]) != i:
                res = [i, save.get(target - nums[i])]
                break
        return res

