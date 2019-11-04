n = 52

s = {}
for i in range(65, 91):
    s[i - 64] = chr(i)

ans = ''
while n != 0:
    if n == 26:
        ans = 'Z' + ans
        break
    cur = n % 26
    if cur == 0:
        ans = 'Z' + ans
        n -= 26
        n = n // 26
    else:
        ans = s[cur] + ans
        n -= cur
        n = n // 26
print(ans)
