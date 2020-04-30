class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:

        d = collections.Counter(nums)

        return sum((k > 0 and ele + k in d) or (k == 0 and d[ele] >= 2) for ele in d)