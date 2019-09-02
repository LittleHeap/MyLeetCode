N = 10

d = {0: 0, 1: 1, 8: 8, 2: 5, 5: 2, 6: 9, 9: 6}

res = []
ans = 0
for num in range(1, N + 1):
    new = []
    num = list(str(num))
    for digit in num:
        if d.get(int(digit)) is not None:
            new.append(str(d.get(int(digit))))
        else:
            break
    if new != num and len(new) == len(num):
        ans = ans + 1
        res.append([''.join(num), ''.join(new)])

print(ans)
print(res)
