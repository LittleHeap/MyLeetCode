class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        s = set()

        for ele in nums:
            if ele not in s:
                s.add(ele)
            else:
                s.remove(ele)

        for res in s:
            return res