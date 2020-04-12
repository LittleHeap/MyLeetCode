class Solution:
    def partition(self, s: str) -> List[List[str]]:

        d = {}

        def isPali(string):
            return string == string[::-1]

        def deep(cur):
            if not cur:
                return [[]]
            else:
                if cur in d:
                    return d[cur]
                res = []
                for i in range(1, len(cur) + 1):
                    if isPali(cur[:i]):
                        for ele in deep(cur[i:]):
                            res.append([cur[:i]] + ele)
                d[cur] = res
                return res

        return deep(s)