class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = {}

        for i in range(len(strs)):
            s = strs[i]
            s = list(s)
            s.sort()
            if tuple(s) in d:
                d[tuple(s)].append(i)
            else:
                d[tuple(s)] = [i]

        res = []
        for ele in d:
            cur = []
            for index in d[ele]:
                cur.append(strs[index])
            res.append(cur)
        return res
