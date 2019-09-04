save = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
s = "MCMXCIV"

pre = 'I'
ans = 0
for i in range(len(s) - 1, -1, -1):
    if save.get(s[i]) < save.get(pre):
        ans -= save.get(s[i])
        pre = s[i]
    else:
        ans += save.get(s[i])
        pre = s[i]

print(ans)

