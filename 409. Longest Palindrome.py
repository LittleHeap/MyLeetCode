class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = collections.Counter(s)

        res = 0
        flag = 1
        for ele in d:
            if d[ele] % 2 == 0:
                res += d[ele]
            else:
                if flag:
                    res += d[ele] - 1
                    res += 1
                    flag = 0
                else:
                    res += d[ele] - 1

        return res