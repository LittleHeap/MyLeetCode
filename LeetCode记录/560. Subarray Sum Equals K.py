nums = [1, 1, 1]
k = 2

d = {}
ans = 0

d[0] = 1
s = 0
for ele in nums:
    s = s + ele
    if d.get(s - k) is not None:
        ans = ans + d.get(s - k)
    d[s] = d.get(s, 0) + 1

print(d)
print(ans)
