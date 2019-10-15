class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        w = []
        c = 0
        res = []
        for i in range(len(words)):
            if c + len(words[i]) + len(w) <= maxWidth:
                w.append(words[i])
                c += len(words[i])
            else:
                n = len(w)
                if n != 1:
                    space = maxWidth - c
                    avg = space // (n - 1)
                    extra = space - avg * (n - 1)
                    cur = ""
                    for j in range(n - 1):
                        cur += w[j]
                        for _ in range(avg):
                            cur += ' '
                        if extra > 0:
                            cur += ' '
                            extra -= 1
                    cur += w[-1]
                else:
                    cur = ''
                    cur += w[0]
                    for _ in range(maxWidth - len(w[0])):
                        cur += ' '
                res.append(cur)
                w = [words[i]]
                c = len(words[i])

        cur = ''
        for i in range(len(w)):
            cur += w[i] + ' '
        for _ in range(maxWidth - c - len(w)):
            cur += ' '
        cur = cur[:maxWidth]

        res.append(cur)
        return res
