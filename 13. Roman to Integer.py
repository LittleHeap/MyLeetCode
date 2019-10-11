class Solution:
    def romanToInt(self, s: str) -> int:
        save = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        res = 0
        pre = None
        for i in range(len(s) - 1, -1, -1):
            if pre is None:
                res += save[s[i]]
                pre = save[s[i]]
            else:
                cur = save[s[i]]
                if cur < pre:
                    res -= cur
                    pre = cur
                else:
                    res += cur
                    pre = cur

        return res