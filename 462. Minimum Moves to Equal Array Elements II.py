class Solution:
    def minMoves2(self, nums: List[int]) -> int:

        nums.sort()

        med = 0
        if len(nums) % 2 == 1:
            med = nums[len(nums) // 2]
        else:
            med = (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) // 2

        res = 0
        for ele in nums:
            res += abs(med - ele)

        return res