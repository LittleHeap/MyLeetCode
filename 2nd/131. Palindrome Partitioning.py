class Solution:
    def partition(self, s: str) -> List[List[str]]:

        S = list(s)
        S.reverse()
        S = ''.join(S)

        n = len(s)
        res = []

        def deep(cur):
            if cur[-1] == n:
                now = []
                for index in range(1, len(cur)):
                    now.append(s[cur[index - 1]: cur[index]])
                res.append(now)
                return
            for k in range(cur[-1] + 1, n + 1):
                if s[cur[-1]: k] == S[n - k: n - cur[-1]]:
                    newcur = cur.copy()
                    newcur.append(k)
                    deep(newcur)

        deep([0])
        return res
