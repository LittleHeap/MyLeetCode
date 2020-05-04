class Solution:
    def findContestMatch(self, n: int) -> str:

        def deep(cur):
            if len(cur) == 1:
                return cur
            newcur = []
            for i in range(len(cur) // 2):
                newcur.append([cur[i], cur[-i - 1]])
            return deep(newcur)

        temp = deep([i for i in range(1, n + 1)])
        # print(temp)

        res = ''

        def recover(temp, res):
            # print(temp)
            if len(temp) == 2 and isinstance(temp[0], int):
                return str(temp[0]) + ',' + str(temp[1])
            cur = ''
            for i, ele in enumerate(temp):
                cur += '(' + recover(ele, res) + ')' + ','
            res = cur[:-1]
            return res

        return recover(temp, res)

