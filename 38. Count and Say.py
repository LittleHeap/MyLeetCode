class Solution:
    def countAndSay(self, n: int) -> str:

        if n == 1:
            return '1'

        cur = [1]

        for _ in range(n - 1):
            new = []
            print(cur)
            c = 1
            for i in range(1, len(cur)):
                if cur[i] == cur[i - 1]:
                    c += 1
                else:
                    new.append(c)
                    new.append(cur[i - 1])
                    c = 1
            new.append(c)
            new.append(cur[-1])
            cur = new

        res = ''
        for ele in cur:
            res += str(ele)

        return res