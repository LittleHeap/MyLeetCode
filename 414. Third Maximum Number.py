class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return max(nums)

        res = []
        hold = set()
        for ele in nums:
            if ele not in hold:
                hold.add(ele)
                heapq.heappush(res, -ele)

        if len(res) <= 2:
            return -min(res)

        heapq.heappop(res)
        heapq.heappop(res)
        return -heapq.heappop(res)