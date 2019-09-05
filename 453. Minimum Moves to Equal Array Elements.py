class Solution:
    def minMoves(self, nums: List[int]) -> int:
        small = min(nums)
        return sum(nums) - small * len(nums)
