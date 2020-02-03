class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        right = sorted(nums)

        n = len(nums)

        start = 0
        end = -1
        for i in range(n):
            if nums[i] != right[i]:
                start = i
                break

        for j in range(n - 1, -1, -1):
            if nums[j] != right[j]:
                end = j
                break

        return end - start + 1