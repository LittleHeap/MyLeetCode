class Solution:
    def arrayNesting(self, nums: List[int]) -> int:

        def helper(index, res):
            if nums[index] is None:
                return res
            next = nums[index]
            nums[index] = None
            return helper(next, res + 1)

        res = 0

        for ele in nums:
            if ele is not None:
                res = max(res, helper(ele, 0))

        return res