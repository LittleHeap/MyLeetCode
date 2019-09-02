licensePlate = "1s3 456"
words = ["looks", "pest", "stew", "show"]

chars = set()
for i in range(ord('a'), ord('z') + 1):
    chars.add(chr(i))
for i in range(ord('A'), ord('Z') + 1):
    chars.add(chr(i))

d = {}
for c in licensePlate:
    if c in chars:
        d[c.lower()] = d.get(c.lower(), 0) + 1

print(d)

res = []
for w in words:
    w = w.lower()
    flag = 1
    for item in d.items():
        if w.count(item[0]) < item[1]:
            flag = 0
            break
    if flag:
        res.append(w)

print(res)
m = 100000000
index = 0
for i in range(len(res)):
    if len(res[i]) < m:
        m = len(res[i])
        index = i

print(res[index])
