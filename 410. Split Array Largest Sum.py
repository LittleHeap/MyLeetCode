class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:

        l = max(nums)
        r = sum(nums)

        while l < r:
            he = (l + r) // 2
            cur = 0
            times = 1
            for num in nums:
                if cur + num <= he:
                    cur += num
                else:
                    cur = num
                    times += 1
            if times <= m:
                r = he
            else:
                l = he + 1

        return l