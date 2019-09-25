class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        k %= n
        temp = nums[-k:]
        for i in range(n - 1, k - 1, -1):
            nums[i] = nums[i - k]
        for i in range(k):
            nums[i] = temp[i]
