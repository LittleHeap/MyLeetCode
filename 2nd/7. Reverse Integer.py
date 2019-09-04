class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        num = list(str(x))
        if x < 0:
            flag = 1
            num.pop(0)
        else:
            flag = 0
        res = []
        i = 0
        num.reverse()
        print(num)
        while i < len(num) and num[i] == '0':
            i += 1
        res = num[i:]
        if flag:
            res.insert(0, '-')
        res = int(''.join(res))
        if res < 2147483647 and res > -2147483648:
            return res
        else:
            return 0
