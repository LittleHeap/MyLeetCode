class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        line1 = set(list('qwertyuiop'))
        line2 = set(list('asdfghjkl'))
        line3 = set(list('zxcvbnm'))

        res = []
        for word in words:
            cur = set(list(word.lower()))
            if cur <= line1 or cur <= line2 or cur <= line3:
                res.append(word)

        return res