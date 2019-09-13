class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(a)
        b = list(b)

        na = len(a)
        nb = len(b)

        flag = 0

        index = -1

        while -index <= na and -index <= nb:
            cura = int(a[index])
            curb = int(b[index])
            cur = cura + curb + flag
            flag = cur // 2
            a[index] = str(cur % 2)
            index -= 1

        while -index <= na:
            cura = int(a[index])
            cur = cura + flag
            flag = cur // 2
            a[index] = str(cur % 2)
            index -= 1
        while -index <= nb:
            curb = int(b[index])
            cur = curb + flag
            flag = cur // 2
            a.insert(0, str(cur % 2))
            index -= 1

        if flag:
            a.insert(0, '1')

        return ''.join(a)