class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:

        degree = sorted(collections.Counter(nums).items(), key=lambda x: x[1])[-1][1]

        res = float('inf')
        cur = defaultdict(int)
        start = 0
        for end in range(len(nums)):
            cur[nums[end]] += 1
            if cur[nums[end]] == degree:
                while nums[start] != nums[end]:
                    cur[nums[start]] -= 1
                    start += 1
                res = min(res, end - start + 1)
        return res
