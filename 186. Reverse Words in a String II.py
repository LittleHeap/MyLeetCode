class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        temp = ''.join(s)
        temp = temp.split(' ')
        temp.reverse()

        res = []
        for c in temp:
            for e in c:
                res.append(e)
            res.append(' ')
        for i in range(len(s)):
            s[i] = res[i]