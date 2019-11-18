class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        if not strings:
            return []
        d = {}
        for ele in strings:
            n = len(ele)
            gap = []
            for i in range(1, n):
                g = ord(ele[i]) - ord(ele[i - 1])
                if g < 0:
                    g += 26
                gap.append(g)
            if (n, tuple(gap)) not in d:
                d[(n, tuple(gap))] = [ele]
            else:
                d[(n, tuple(gap))].append(ele)

        res = []
        for ele in d.values():
            res.append(ele)
        return res