class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:

        if not d:
            return ''

        l = 0
        cur = max(d)

        def match(a, b):
            index = -1
            for char in b:
                index = a.find(char, index + 1)
                if index < 0:
                    return False
            return True

        for word in d:
            if match(s, word):
                if len(word) > l:
                    l = len(word)
                    cur = word
                elif len(word) == l:
                    cur = min(cur, word)

        if l == len(cur):
            return cur
        else:
            return ''