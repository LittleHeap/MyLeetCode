class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        if n <= 1:
            return nums

        i = n - 2
        res = [nums[-1]]

        while i >= 0 and nums[i] >= nums[i + 1]:
            res.append(nums[i])
            i -= 1
        if i == -1:
            nums.sort()
        else:
            res.sort()
            for j in range(len(res)):
                if res[j] > nums[i]:
                    res[j], nums[i] = nums[i], res[j]
                    index = 0
                    for k in range(i + 1, n):
                        nums[k] = res[index]
                        index += 1
                    break