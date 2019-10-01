s = "010010"

n = len(s)

res = []


def deep(cur, num):
    if num > 4 or (num < 4 and cur[-1] == n):
        return
    if num == 4:
        if cur[-1] == n:
            ans = ''
            ans += s[cur[0]:cur[1]] + '.' + s[cur[1]:cur[2]] + '.' + s[cur[2]:cur[3]] + '.' + s[cur[3]:]
            res.append(ans)
            return
        else:
            return
    if s[cur[-1]] == '0':
        newcur = cur.copy()
        newcur.append(cur[-1] + 1)
        deep(newcur, num + 1)
    else:
        for i in range(cur[-1] + 1, cur[-1] + 4):
            if i > n:
                return
            if int(s[cur[-1]: i]) <= 255:
                newcur = cur.copy()
                newcur.append(i)
                deep(newcur, num + 1)


deep([0], 0)
print(res)
