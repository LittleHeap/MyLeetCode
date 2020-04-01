class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        d = {}
        for i in range(len(order)):
            d[order[i]] = i

        save = {}

        for i, word in enumerate(words):
            cur = []
            for char in word:
                cur.append(d[char])
            save[i] = tuple(cur)
            if i == 0:
                continue
            elif save[i - 1] > save[i]:
                return False

        return True