class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator * denominator < 0:
            flag = 1
        else:
            flag = 0

        numerator = abs(numerator)
        denominator = abs(denominator)

        res = []
        s = {}

        i = 0
        l = numerator // denominator
        res.append(str(l))
        remain = numerator - l * denominator
        if remain == 0:
            if flag:
                res[0] = -int(res[0])
            return str(res[0])
        s[remain] = i
        i += 1
        while remain < denominator:
            if i == 1:
                res.append('.')
            s[remain] = i
            i += 1
            remain *= 10
            res.append('0')
        res.pop()

        while 1 and remain != 0:
            if i == 1:
                res.append('.')
            cur = remain // denominator
            remain = remain - cur * denominator
            res.append(str(cur))

            if remain in s or remain == 0:
                break
            else:
                while remain != 0 and remain < denominator:
                    s[remain] = i
                    i += 1
                    remain *= 10
                    res.append('0')
                res.pop()

        if remain != 0:
            index = s.get(remain)
            res.insert(index + 1, '(')
            res.append(')')

        if flag:
            res.insert(0, '-')

        return ''.join(res)
