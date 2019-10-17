class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []

        def deep(cur, level):
            if level == 0:
                for i in range(1, n + 1):
                    newcur = cur.copy()
                    newcur.append(i)
                    if level + 1 == k:
                        res.append(newcur)
                    else:
                        deep(newcur, level + 1)
            else:
                for i in range(cur[-1] + 1, n + 1):
                    newcur = cur.copy()
                    newcur.append(i)
                    if level + 1 == k:
                        res.append(newcur)
                    else:
                        deep(newcur, level + 1)

        deep([], 0)
        return res
