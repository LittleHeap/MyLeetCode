class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d = defaultdict(int)

        res = 0
        for ele in nums:
            d[ele] += 1
            res = max(res, (d[ele] + d[ele + 1] if d[ele + 1] > 0 else 0),
                      (d[ele] + d[ele - 1] if d[ele - 1] > 0 else 0))

        return res