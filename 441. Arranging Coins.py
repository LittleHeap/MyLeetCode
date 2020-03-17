class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        s = set()

        res = []

        for ele in nums:
            if ele in s:
                res.append(ele)
            else:
                s.add(ele)

        return res