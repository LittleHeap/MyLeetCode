class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        m = str(bin(m))[2:]
        n = str(bin(n))[2:]

        lm = len(m)
        ln = len(n)

        if lm != ln:
            return 0
        else:
            for i in range(lm):
                if m[i] != n[i]:
                    m = m[:i]
                    ap = ''
                    for _ in range(lm - i):
                        ap += '0'
                    m += ap
                    break

        return int(m, 2)