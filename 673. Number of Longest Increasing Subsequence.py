class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        if not nums:
            return 0

        for i, ele in enumerate(nums):
            if i == 0:
                nums[i] = [nums[i], 1, 1]
            else:
                l = 1
                num = 1
                for j in range(i):
                    if ele > nums[j][0]:
                        if nums[j][1] + 1 > l:
                            l = nums[j][1] + 1
                            num = nums[j][2]
                        elif nums[j][1] + 1 == l:
                            num += nums[j][2]
                nums[i] = [ele, l, num]

        temp = max(nums, key=lambda x: x[1])[1]

        return sum([(ele[2] if ele[1] == temp else 0) for ele in nums])


