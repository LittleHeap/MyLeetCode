import bisect
s = 'zafb'

s = sorted(list(s))
print(s)

cur = [s.pop(0)]
flag = 1
while s:
    if cur[-1] == s[0] and cur[-1] == s[-1]:
        cur.extend(s)
        break
    if flag == 1:
        index = bisect.bisect_right(s, cur[-1])
        if index != len(s):
            cur.append(s.pop(index))
        else:
            flag = -1
    elif flag == -1:
        index = bisect.bisect_left(s, cur[-1])
        if index != 0:
            cur.append(s.pop(index - 1))
        else:
            flag = 1

print(cur)
