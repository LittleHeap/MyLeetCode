class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        cul = 0
        s = {}

        res = 0
        for ele in nums:
            cul += ele
            s[cul] = s.get(cul, 0) + 1
            if cul - k in s:
                res += s[cul - k]
                if k == 0:
                    res -= 1
            if cul == k:
                res += 1

        return res
