class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = {}

        for ele in strs:
            l = list(ele)
            l.sort()
            l = ''.join(l)
            if l not in d:
                d[l] = [ele]
            else:
                d[l].append(ele)

        res = []
        for ele in d.items():
            res.append(ele[1])
        return res
