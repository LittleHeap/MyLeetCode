class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        d1 = {}
        d2 = []

        for i, s in enumerate(logs):
            if s.split(' ')[1].isdigit():
                d2.append(s)
            else:
                index = s.index(' ')
                if s[index + 1:] in d1:
                    d1[s[index + 1:]].append(i)
                else:
                    d1[s[index + 1:]] = [i]

        d1 = sorted(list(d1.items()))
        res = []

        for ele in d1:
            cur = []
            for index in ele[1]:
                cur.append(logs[index])
            cur.sort()
            res.extend(cur)

        for ele in d2:
            res.append(ele)

        return res