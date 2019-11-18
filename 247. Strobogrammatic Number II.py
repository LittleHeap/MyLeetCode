class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:

        if n == 1:
            return ["0", "1", "8"]
        d = {}
        d[0] = 0
        d[1] = 1
        d[6] = 9
        d[8] = 8
        d[9] = 6

        hold = [0, 1, 6, 8, 9]
        half = (n - 1) // 2

        res = []

        def deep(cur, index):
            if index <= half:
                if index == 0:
                    for i in range(1, 5):
                        newcur = cur
                        newcur += str(hold[i])
                        deep(newcur, index + 1)
                elif index == half and n % 2 == 1:
                    for c in ['0', '1', '8']:
                        newcur = cur
                        newcur += c
                        deep(newcur, index + 1)
                else:
                    for i in range(5):
                        newcur = cur
                        newcur += str(hold[i])
                        deep(newcur, index + 1)
            else:
                if n % 2 == 0:
                    i = len(cur) - 1
                    ans = cur
                    while i >= 0:
                        ans += str(d[int(cur[i])])
                        i -= 1
                    res.append(ans)
                else:
                    i = len(cur) - 2
                    ans = cur
                    while i >= 0:
                        ans += str(d[int(cur[i])])
                        i -= 1
                    res.append(ans)

        deep('', 0)
        return res