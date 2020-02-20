class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        if a == 0:
            res = []
            for ele in nums:
                res.append(b * ele + c)
            if b < 0:
                res.reverse()
            return res

        mid = - b / (2 * a)

        dis = float('inf')

        index = 0
        for i in range(len(nums)):
            if abs(nums[i] - mid) < dis:
                index = i
                dis = abs(nums[i] - mid)

        res = []
        while nums:
            res.append(a * (nums[index] ** 2) + b * nums[index] + c)
            if index + 1 < len(nums) and index - 1 >= 0:
                if abs(nums[index + 1] - mid) < abs(nums[index - 1] - mid):
                    nums.pop(index)
                else:
                    nums.pop(index)
                    index -= 1
            elif index + 1 < len(nums):
                nums.pop(index)
            elif index - 1 >= 0:
                nums.pop(index)
                index -= 1
            else:
                nums.pop(index)
        if a < 0:
            res.reverse()

        return res
