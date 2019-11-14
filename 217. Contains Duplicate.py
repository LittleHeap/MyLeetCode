class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = set()
        for ele in nums:
            if ele not in d:
                d.add(ele)
            else:
                return True
        return False