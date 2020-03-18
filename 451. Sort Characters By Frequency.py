class Solution:
    def frequencySort(self, s: str) -> str:

        d = collections.Counter(s)

        res = sorted(d.items(), key=lambda x: x[1], reverse=True)

        ans = ''

        for ele in res:
            for _ in range(ele[1]):
                ans += ele[0]

        return ans