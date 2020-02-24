class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        for i in range(1, n + 1):
            heapq.heappush(res, str(i))

        ans = []
        while res:
            ans.append(heapq.heappop(res))

        ans = list(map(int, ans))

        return ans