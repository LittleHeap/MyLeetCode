class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        hold = []

        res = []

        temp = collections.Counter(words)

        for ele in temp.items():
            heapq.heappush(hold, (-ele[1], ele[0]))

        i = 0
        while i + 1 <= k:
            node = heapq.heappop(hold)
            cur = [node[1]]
            count = node[0]
            i += 1
            while i + 1 <= k and hold[0][0] == count:
                heapq.heappush(cur, heapq.heappop(hold)[1])
                i += 1
            res.extend(cur)

        return res