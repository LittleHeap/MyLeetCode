class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        n = len(nums)
        t = n // 3
        d = {}
        res = []
        for ele in nums:
            d[ele] = d.get(ele, 0) + 1

        for ele in d.items():
            if ele[1] > t:
                res.append(ele[0])

        return res
