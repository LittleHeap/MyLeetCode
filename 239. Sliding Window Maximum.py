import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        n = len(nums)
        cur = nums[:k]
        heapq.heapify(cur)
        res = []
        res.append(heapq.nlargest(1, cur)[0])

        for i in range(k, n):
            cur.remove(nums[i - k])
            heapq.heappush(cur, nums[i])
            res.append(heapq.nlargest(1, cur)[0])
        return res