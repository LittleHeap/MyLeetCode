class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        d = defaultdict(list)

        for word in products:
            cur = ''
            for char in word:
                cur += char
                heapq.heappush(d[cur], word)

        res = []

        cur = ''
        for char in searchWord:
            temp = []
            cur += char
            for _ in range(3):
                if d[cur]:
                    temp.append(heapq.heappop(d[cur]))
                else:
                    break
            res.append(temp)

        return res