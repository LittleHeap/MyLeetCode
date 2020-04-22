class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        [nums.insert(i, (nums.pop() if i % 2 == 1 else nums.pop((len(nums) + 1) // 2 - 1 + i // 2))) for i in
         range(len(nums))]

