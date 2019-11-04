s = "eceba"

window = []
cur = []
ans = 0

for i, c in enumerate(s):
    if len(cur) <= 1:
        window.append(c)
        if c not in cur:
            cur.append(c)
    elif len(cur) == 2 and c in cur:
        window.append(c)
    else:
        hold = window[-1]
        for j in range(len(window) - 1, - 1, -1):
            if window[j] != hold:
                cur.remove(window[j])
                window = window[j + 1:]
                break
        window.append(c)
        cur.append(c)
    ans = max(ans, len(window))

print(ans)