s = "ZY"

ans = 0
cur = 26
m = 0
for i in range(len(s) - 1, -1, -1):
    ans += (ord(s[i]) - 64) * (26 ** m)
    m += 1

print(ans)
