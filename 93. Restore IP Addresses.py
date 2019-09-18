class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        if len(s) > 12 or len(s) <= 3:
            return []

        s = list(s)
        n = len(s)

        res = []
        for i1 in range(1, 4):
            if s[0] == '0' and i1 >= 2:
                continue
            for i2 in range(i1 + 1, i1 + 4):
                if s[i1] == '0' and i2 - i1 >= 2:
                    continue
                for i3 in range(i2 + 1, i2 + 4):
                    if i3 >= n:
                        continue
                    if s[i2] == '0' and i3 - i2 >= 2:
                        continue
                    if s[i3] == '0' and n - i3 >= 2:
                        continue
                    if n - i3 <= 3 and n - i3 >= 1 and int(''.join(s[:i1])) <= 255 and int(
                            ''.join(s[i1: i2])) <= 255 and int(
                        ''.join(s[i2: i3])) <= 255 and int(''.join(s[i3:])) <= 255:
                        now = s.copy()
                        now.insert(i1, '.')
                        now.insert(i2 + 1, '.')
                        now.insert(i3 + 2, '.')
                        res.append(''.join(now))

        return (res)
