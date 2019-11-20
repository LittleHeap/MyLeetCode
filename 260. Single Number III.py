class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        s = set()

        for ele in nums:
            if ele not in s:
                s.add(ele)
            else:
                s.remove(ele)
        return list(s)