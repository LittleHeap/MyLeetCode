arr = [3,2,1,2,7]

t = set(arr)
c = set()

res = 0
for num in arr:
    if num not in c:
        res += num
        c.add(num)
    else:
        cur = num + 1
        while cur in t:
            cur += 1
        res += cur
        t.add(cur)

print(res)