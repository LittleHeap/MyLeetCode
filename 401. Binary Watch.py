class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        h = [1, 2, 4, 8]
        m = [1, 2, 4, 8, 16, 32]

        res = []
        for i in range(num + 1):
            l = i
            r = num - i
            ll = list(itertools.combinations(h, l))
            mm = list(itertools.combinations(m, r)) 
            for a in ll:
                if len(a) == 0:
                    a = '0'
                else:
                    a = sum(a)
                    if a >= 12:
                        continue
                    a = str(a)
                for b in mm:
                    if len(list(b)) == 0:
                        b = '00'
                    else:
                        b = sum(b)
                        if b >= 60:
                            continue
                        if len(str(b)) == 1:
                            b = '0' + str(b)
                        else:
                            b = str(b)
                    res.append(a + ':' + b)
        return res