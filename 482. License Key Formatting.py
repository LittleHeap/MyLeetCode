class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = ''.join(S.split('-')).upper()

        if K >= len(S):
            return S.upper()

        res = ''
        for i in range(len(S) - K, -1, -K):
            res = S[i:i + K] + '-' + res
            if i > 0 and i - K < 0:
                res = S[:i] + '-' + res
                break

        res = res[:-1]
        return res