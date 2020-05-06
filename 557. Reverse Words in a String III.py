class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        res = []
        for ele in s:
            ele = list(ele)
            ele.reverse()
            res.append(''.join(ele))

        return ' '.join(res)