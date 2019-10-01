class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]

        hold = set()

        res = []

        cur = ['0' for _ in range(n)]
        cur[-1] = '1'
        d = {'1': '0', '0': '1'}

        while len(res) < 2 ** n:
            index = n - 1
            while 1:
                cur[index] = d[cur[index]]
                if ''.join(cur) not in hold:
                    res.append(int(''.join(cur), 2))
                    hold.add(''.join(cur))
                    break
                else:
                    cur[index] = d[cur[index]]
                    index -= 1
                    index %= n
        return res
