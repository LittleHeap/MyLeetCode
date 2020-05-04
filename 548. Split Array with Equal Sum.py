class Solution:
    def splitArray(self, nums: List[int]) -> bool:

        cul = []

        for i in range(len(nums)):
            if i == 0:
                cul.append(nums[i])
            else:
                cul.append(nums[i] + cul[-1])

        def helper(cur, fund):
            res = set()
            for i in range(1, len(cur) - 1):
                if cur[i - 1] - fund == cur[-1] - cur[i]:
                    res.add(cur[i - 1] - fund)
            return res

        for i in range(1, len(nums) - 1):
            res1, res2 = None, None
            res1 = helper(cul[:i], 0)
            res2 = helper(cul[i + 1:], cul[i])
            if len(res1 & res2) >= 1:
                # print(i)
                return True

        return False