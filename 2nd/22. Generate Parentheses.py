n = 3

res = []


def deep(cur, l, r):
    if l == n and r == n:
        res.append(cur)
        return
    if l > r:
        deep(cur + ')', l, r + 1)
    if l < n:
        deep(cur + '(', l + 1, r)


deep('', 0, 0)
print(res)
