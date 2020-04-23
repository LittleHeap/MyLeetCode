class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        stack, res = [], [-1 for _ in range(len(nums))]

        for i in [j for j in range(len(nums))] * 2:
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            stack.append(i)

        return res