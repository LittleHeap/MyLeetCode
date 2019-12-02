import bisect

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        data = []
        res = []
        c = 0

        for i in range(len(nums) - 1, -1, -1):
            index = bisect.bisect_left(data, nums[i])
            data.insert(index, nums[i])
            res.append(index)

        res.reverse()
        return res