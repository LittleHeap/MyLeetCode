class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        s = set()
        for ele in nums:
            if ele not in s:
                s.add(ele)
            else:
                return ele