class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        n = len(nums)
        half = n // 2

        d = {}

        for ele in nums:
            d[ele] = d.get(ele, 0) + 1
            if d[ele] > half:
                return ele