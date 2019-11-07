a = [25, 35, 872, 228, 53, 278, 872]

temp = []
for ele in a:
    cur = sorted(str(ele), reverse=True)
    cur = int(''.join(cur))
    temp.append(cur)


d = {}
for ele in temp:
    d[ele] = d.get(ele,0) + 1

ans = 0
for ele in d.items():
    ans += ele[1] * (ele[1] - 1) // 2
print(ans)
