class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        cur = 0
        curl = []
        start = 0
        stop = -1

        res = []
        for i, ele in enumerate(words):
            l = len(ele)
            if cur + l <= maxWidth:
                cur += l + 1
                curl.append(l)
                stop += 1
            else:
                if len(curl) == 1:
                    sp = maxWidth - curl[0]
                    now = ''
                    now += words[i - 1]
                    for t in range(sp):
                        now += ' '
                    res.append(now)
                else:
                    leftsp = maxWidth - sum(curl)
                    sp = leftsp // (len(curl) - 1)
                    leftsp = leftsp - sp * (len(curl) - 1)
                    now = ''
                    for k in range(start, stop):
                        now += words[k]
                        for s in range(sp):
                            now += ' '
                        if leftsp > 0:
                            now += ' '
                            leftsp -= 1
                    now += words[stop]
                    res.append(now)
                curl = [l]
                start = i
                stop = i
                cur = l + 1

        leftsp = maxWidth - sum(curl)
        leftsp -= len(curl)
        now = ''
        for ele in words[start:]:
            now += ele
            now += ' '
        for s in range(leftsp):
            now += ' '
        if len(now) > maxWidth:
            now = now[:-1]
        res.append(now)
        return (res)