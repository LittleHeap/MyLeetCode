class Solution:
    def triangleNumber(self, nums: List[int]) -> int:

        nums.sort()

        res = 0
        for i in range(len(nums) - 1, 1, -1):
            low = 0
            high = i - 1
            while low < high:
                if nums[low] + nums[high] > nums[i]:
                    res += high - low
                    high -= 1
                else:
                    low += 1

        return res

