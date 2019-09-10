class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = {}

        for ele in strs:
            e = list(ele)
            e.sort()
            e = ''.join(e)
            d[e] = d.get(e, [])
            d[e].append(ele)

        res = []
        for item in d.items():
            res.append(item[1])

        return res