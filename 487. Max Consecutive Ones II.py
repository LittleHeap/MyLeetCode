class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        if not nums:
            return 0

        l, r = 0, 0
        res = 0
        n = len(nums)
        flag = 1
        while r < n and nums[r] == 0:
            r += 1
            l += 1

        while r < n:
            print(l, r)
            if r + 1 < n and nums[r + 1] == 1:
                r += 1
                res = max(res, r - l + 1)
            else:
                res = max(res, r - l + 1)
                if r + 1 < n and flag:
                    res = max(res, r - l + 2)
                if l - 1 >= 0 and flag:
                    res = max(res, r - l + 2)
                if r + 2 < n and nums[r + 2] == 1:
                    if flag:
                        r += 1
                        flag = 0
                        mark = r + 1
                    else:
                        res = max(res, r - l + 1)
                        r += 1
                        l = mark
                        mark = r + 1
                        flag = 0
                else:
                    res = max(res, r - l + 1)
                    r += 2
                    l = r
                    while r < n and nums[r] != 1:
                        r += 1
                        l += 1
                    flag = 1

        if res == 0:
            return 1
        return res
