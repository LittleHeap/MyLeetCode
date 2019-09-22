class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        d = {}
        for ele in nums:
            d[ele] = d.get(ele, 0) + 1
            if d.get(ele) == 3:
                d.pop(ele)

        return list(d.items())[0][0]
