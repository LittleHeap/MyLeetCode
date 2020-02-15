class Solution:
    def reverseVowels(self, s: str) -> str:

        v = set()
        v.add('a')
        v.add('e')
        v.add('i')
        v.add('o')
        v.add('u')
        v.add('A')
        v.add('E')
        v.add('I')
        v.add('O')
        v.add('U')

        vowel = []
        index = set()

        for i in range(len(s)):
            if s[i] in v:
                vowel.append(s[i])
                index.add(i)

        res = []
        for i in range(len(s)):
            if i not in index:
                res.append(s[i])
            else:
                res.append(vowel.pop())

        return ''.join(res)

