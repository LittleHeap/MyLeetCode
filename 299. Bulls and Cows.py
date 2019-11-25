class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        s = []

        d = {'A': 0, 'B': 0}
        n = len(secret)
        hs = []
        hg = []
        for i in range(n):
            if secret[i] != guess[i]:
                hs.append(secret[i])
                hg.append(guess[i])
            else:
                d['A'] += 1

        for ele in hs:
            if ele in hg:
                hg.remove(ele)
                d['B'] += 1

        return str(d['A']) + 'A' + str(d['B']) + 'B'