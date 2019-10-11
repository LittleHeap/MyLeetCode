class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ''

        n = float('inf')

        for word in strs:
            n = min(n, len(word))

        l = len(strs)
        i = 0
        res = ''
        while i < n:
            flag = 0
            for k in range(1, l):
                if strs[k][i] != strs[k - 1][i]:
                    flag = 1
                    break
            if flag:
                break
            else:
                res += strs[0][i]
            i += 1

        return res