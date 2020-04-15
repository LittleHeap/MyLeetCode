class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:

        cur = [lower - 1] + nums + [upper + 1]

        res = []
        for i in range(1, len(cur)):
            if cur[i] - cur[i - 1] == 2:
                res.append(str(cur[i] - 1))
            elif cur[i] - cur[i - 1] > 2:
                res.append(str(cur[i - 1] + 1) + '->' + str(cur[i] - 1))

        return res
