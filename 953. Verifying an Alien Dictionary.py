words = ["apple", "app"]
order = "abcdefghijklmnopqrstuvwxyz"


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {}
        for i, char in enumerate(order):
            d[char] = i

        for i in range(len(words) - 1):
            a = words[i]
            b = words[i + 1]
            for j in range(min(len(a), len(b))):
                if d.get(a[j]) < d.get(b[j]):
                    break
                elif d.get(a[j]) > d.get(b[j]):
                    return False
                    break
            if d.get(a[j]) == d.get(b[j]) and len(words[i]) > len(words[i + 1]):
                return False
        return True
