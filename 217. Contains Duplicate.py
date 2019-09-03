class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        have = set()
        for ele in nums:
            if ele not in have:
                have.add(ele)
            else:
                return True
        return False
